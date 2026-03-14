import os
import json
import requests
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# =========================
# CONFIG
# =========================
EMBED_PKL_PATH = r"C:\Users\LENOVO\.cursor\python_oneshot\final_project\embedded_chunks.pkl"
OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
OLLAMA_GENERATE_URL = "http://localhost:11434/api/generate"

EMBED_MODEL = "bge-m3"
LLM_MODEL = "llama3.2"

TOP_RESULTS = 5
CHAT_HISTORY_FILE = "conversation_history.json"
PROMPT_LOG_FILE = "last_prompt.txt"
RESPONSE_LOG_FILE = "last_response.txt"


# =========================
# EMBEDDING FUNCTION
# =========================
def create_embedding(text_list):
    """
    Create embeddings using Ollama embed API.
    """
    response = requests.post(
        OLLAMA_EMBED_URL,
        json={
            "model": EMBED_MODEL,
            "input": text_list
        },
        timeout=120
    )

    response.raise_for_status()
    data = response.json()

    if "embeddings" not in data:
        raise ValueError(f"'embeddings' key missing in response: {data}")

    return data["embeddings"]


# =========================
# LLM INFERENCE FUNCTION
# =========================
def inference(prompt):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        },
        timeout=180
    )

    response.raise_for_status()
    data = response.json()

    if "message" not in data or "content" not in data["message"]:
        raise ValueError(f"Unexpected response format: {data}")

    return data["message"]["content"]


# =========================
# FILE HELPERS
# =========================
def load_dataframe(pkl_path):
    """
    Load embedded dataframe from pickle.
    """
    if not os.path.exists(pkl_path):
        raise FileNotFoundError(f"Pickle file not found: {pkl_path}")

    df = pd.read_pickle(pkl_path)

    if "embeddings" not in df.columns:
        raise KeyError(
            f"'embeddings' column not found in dataframe. Available columns: {list(df.columns)}"
        )

    return df


def load_chat_history(file_path):
    """
    Load existing chat history if available.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_chat_history(history, file_path):
    """
    Save full chat history to JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)


def append_chat_entry(file_path, user_query, answer, retrieved_chunks):
    """
    Append one conversation entry to history file.
    """
    history = load_chat_history(file_path)

    history.append({
        "user_query": user_query,
        "assistant_answer": answer,
        "retrieved_chunks": retrieved_chunks.to_dict(orient="records")
    })

    save_chat_history(history, file_path)


# =========================
# RETRIEVAL FUNCTION
# =========================
def retrieve_relevant_chunks(df, incoming_query, top_k=5):
    """
    Create query embedding, compute cosine similarity,
    and return top-k most relevant chunks.
    """
    question_embedding = create_embedding([incoming_query])[0]

    embeddings_matrix = np.vstack(df["embeddings"].values)
    similarities = cosine_similarity(embeddings_matrix, [question_embedding]).flatten()

    top_indices = similarities.argsort()[::-1][:top_k]
    top_df = df.iloc[top_indices].copy()
    top_df["similarity"] = similarities[top_indices]

    return top_df, question_embedding, similarities


# =========================
# PROMPT BUILDER
# =========================
def build_prompt(retrieved_df, incoming_query):
    """
    Build prompt for the LLM using retrieved chunks.
    """
    available_cols = [col for col in ["title", "number", "start", "end", "text"] if col in retrieved_df.columns]
    context_json = retrieved_df[available_cols].to_json(orient="records", force_ascii=False)

    prompt = f"""
You are a helpful course assistant.

You have access to relevant subtitle/text chunks from a programming course.
Each chunk may contain:
- title
- video number
- start timestamp
- end timestamp
- text

Relevant chunks:
{context_json}

User question:
"{incoming_query}"

Instructions:
1. Answer only from the provided context.
2. Be natural and helpful.
3. Mention which video the user should watch.
4. Mention timestamps wherever possible.
5. If the answer is not clearly available in the provided chunks, say that the available course context does not contain enough information.
6. If the user asks something unrelated to the course content, say that you can only answer questions related to the course material.
7. Do not mention JSON, chunks, embeddings, or internal retrieval process.
"""
    return prompt.strip()


# =========================
# MAIN CHAT LOOP
# =========================
def chat():
    print("Loading embedded chunks...")
    df = load_dataframe(EMBED_PKL_PATH)
    print(f"Loaded dataframe with {len(df)} rows.")

    while True:
        incoming_query = input("\nAsk a Question (or type 'exit'): ").strip()

        if incoming_query.lower() in {"exit", "quit", "q"}:
            print("Exiting chat.")
            break

        if not incoming_query:
            print("Please enter a valid question.")
            continue

        try:
            # Retrieve relevant chunks
            retrieved_df, question_embedding, similarities = retrieve_relevant_chunks(
                df=df,
                incoming_query=incoming_query,
                top_k=TOP_RESULTS
            )

            # Build prompt
            prompt = build_prompt(retrieved_df, incoming_query)

            # Save prompt for debugging
            with open(PROMPT_LOG_FILE, "w", encoding="utf-8") as f:
                f.write(prompt)

            # Generate response
            response_data = inference(prompt)
            answer = response_data["response"]

            print("\nAssistant:\n")
            print(answer)

            # Save last response
            with open(RESPONSE_LOG_FILE, "w", encoding="utf-8") as f:
                f.write(answer)

            # Save conversation entry
            append_chat_entry(
                file_path=CHAT_HISTORY_FILE,
                user_query=incoming_query,
                answer=answer,
                retrieved_chunks=retrieved_df
            )

            # Optional debug preview
            print("\nTop retrieved chunks:")
            preview_cols = [col for col in ["title", "number", "start", "end", "similarity"] if col in retrieved_df.columns]
            print(retrieved_df[preview_cols].to_string(index=False))

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    chat()