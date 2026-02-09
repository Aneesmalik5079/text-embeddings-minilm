from text_embeddings_minilm import get_embedding

if __name__ == "__main__":
    embedding = get_embedding("Testing package import")

    print("Embedding generated successfully")
    print("Embedding length:", len(embedding))
