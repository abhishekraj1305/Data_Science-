import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity

PKL_PATH = r"C:\Users\LENOVO\.cursor\python_oneshot\final_project\embedded_chunks.pkl"
EMBED_URL = "http://localhost:11434/api/embed"
CHAT_URL = "http://localhost:11434/api/chat"

EMBED_MODEL = "bge-m3"
CHAT_MODEL = "llama3.2"

TOP_RESULTS = 30
SIMILARITY_THRESHOLD = 0.70
NEIGHBOR_WINDOW = 1


def create_embedding(text_list):
    r = requests.post(
        EMBED_URL,
        json={"model": EMBED_MODEL, "input": text_list},
        timeout=120
    )
    r.raise_for_status()
    data = r.json()

    if "embeddings" not in data:
        raise ValueError(f"Invalid embedding response: {data}")

    return data["embeddings"]


def inference(prompt):
    r = requests.post(
        CHAT_URL,
        json={
            "model": CHAT_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        },
        timeout=180
    )
    r.raise_for_status()
    data = r.json()

    if "message" not in data or "content" not in data["message"]:
        raise ValueError(f"Invalid chat response: {data}")

    return data["message"]["content"]


df = pd.read_pickle(PKL_PATH)

df = df[df["embeddings"].notna()].copy()
df = df[df["embeddings"].apply(lambda x: isinstance(x, (list, np.ndarray)) and len(x) > 0)].copy()
df = df.reset_index(drop=True)

incoming_query = input("Ask a Question: ").strip()

if not incoming_query:
    print("Please enter a valid question.")
    raise SystemExit

question_embedding = create_embedding([incoming_query])[0]

similarities = cosine_similarity(
    np.vstack(df["embeddings"].values),
    [question_embedding]
).flatten()

df["similarity"] = similarities

top_idx = similarities.argsort()[::-1][:TOP_RESULTS]
top_df = df.iloc[top_idx].copy()
top_df = top_df[top_df["similarity"] >= SIMILARITY_THRESHOLD]

if top_df.empty:
    print("\nAnswer:\n")
    print("I could not find a strong enough answer in the course material.")
    raise SystemExit

expanded_indexes = set()

for idx in top_df.index:
    start_idx = max(0, idx - NEIGHBOR_WINDOW)
    end_idx = min(len(df) - 1, idx + NEIGHBOR_WINDOW)
    expanded_indexes.update(range(start_idx, end_idx + 1))

context_df = df.iloc[sorted(expanded_indexes)].copy()

if "number" in context_df.columns:
    context_df = context_df.sort_values(by=["number", "start"], ascending=[True, True])
elif "start" in context_df.columns:
    context_df = context_df.sort_values(by=["start"], ascending=True)

context_cols = [c for c in ["title", "number", "start", "end", "text"] if c in context_df.columns]

prompt = f"""
You are a helpful assistant for a programming course.

Use only the provided course context.
Do not use outside knowledge.
Do not guess.
If the answer is not clearly present in the context, say:
"I could not find a clear answer in the retrieved course material."

Course context:
{context_df[context_cols].to_json(orient="records", force_ascii=False)}

User question:
"{incoming_query}"

Answer naturally.
Mention:
- video title or number
- relevant timestamps
- what is taught there

If the question is unrelated to the course, say that you can only answer questions related to the course material.
""".strip()

with open("prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)

response = inference(prompt)

with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response)

print("\nAnswer:\n")
print(response)

print("\nTop matched chunks:\n")
show_cols = [c for c in ["title", "number", "start", "end", "similarity", "text"] if c in top_df.columns]
print(top_df[show_cols].to_string(index=False))