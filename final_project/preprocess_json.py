import os
import json
import requests
import pandas as pd


OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
MODEL_NAME = "bge-m3"
JSON_FOLDER = "jsons"


def create_embedding(text_list):
    """
    Create embeddings for a list of text chunks using Ollama.
    Returns a list of embeddings.
    Raises an exception if API response is invalid.
    """
    response = requests.post(
        OLLAMA_EMBED_URL,
        json={
            "model": MODEL_NAME,
            "input": text_list
        },
        timeout=120
    )

    # HTTP-level check
    response.raise_for_status()

    # Parse JSON safely
    data = response.json()

    # Validate response structure
    if "embeddings" not in data:
        raise ValueError(f"'embeddings' key not found in response: {data}")

    return data["embeddings"]


def main():
    json_files = [f for f in os.listdir(JSON_FOLDER) if f.lower().endswith(".json")]

    my_dicts = []
    skipped_files = []          # only filenames
    skipped_file_details = []   # filename + error reason
    chunk_id = 0

    for json_file in json_files:
        file_path = os.path.join(JSON_FOLDER, json_file)
        print(f"\nCreating Embeddings for {json_file}")

        try:
            # Load JSON file
            with open(file_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Validate expected structure
            if "chunks" not in content:
                raise KeyError("'chunks' key not found in JSON")

            if not isinstance(content["chunks"], list):
                raise TypeError("'chunks' must be a list")

            # Extract valid text chunks only
            text_list = []
            valid_chunks = []

            for chunk in content["chunks"]:
                if not isinstance(chunk, dict):
                    continue

                text = chunk.get("text", "")
                if isinstance(text, str) and text.strip():
                    text_list.append(text)
                    valid_chunks.append(chunk)

            if not text_list:
                raise ValueError("No valid text chunks found for embedding")

            # Create embeddings
            embeddings = create_embedding(text_list)

            # Extra validation
            if len(embeddings) != len(valid_chunks):
                raise ValueError(
                    f"Embedding count mismatch. "
                    f"Chunks: {len(valid_chunks)}, Embeddings: {len(embeddings)}"
                )

            # Attach embeddings to chunks
            for i, chunk in enumerate(valid_chunks):
                chunk["chunk_id"] = chunk_id
                chunk["embeddings"] = embeddings[i]
                chunk_id += 1
                my_dicts.append(chunk)

            print(f"Processed successfully: {json_file}")

        except Exception as e:
            print(f"Skipped {json_file} due to error: {e}")
            skipped_files.append(json_file)
            skipped_file_details.append({
                "filename": json_file,
                "error": str(e)
            })
            continue

    # Final DataFrame
    df = pd.DataFrame.from_records(my_dicts)

    print("\n================ FINAL SUMMARY ================")
    print(f"Total processed chunks: {len(my_dicts)}")
    print(f"Total skipped files: {len(skipped_files)}")
    print(f"Skipped filenames: {skipped_files}")

    if skipped_file_details:
        print("\nSkipped file details:")
        for item in skipped_file_details:
            print(f"- {item['filename']} --> {item['error']}")

    # Optional: save outputs
    df.to_pickle("embedded_chunks.pkl")

    with open("skipped_files.json", "w", encoding="utf-8") as f:
        json.dump(skipped_file_details, f, indent=4, ensure_ascii=False)

    return df, skipped_files, skipped_file_details


if __name__ == "__main__":
    df, skipped_files, skipped_file_details = main()