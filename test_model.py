from text_embeddings_minilm.embedder import get_embedding

if __name__ == "__main__":
    text = "Hello world, this is a test"
    embedding = get_embedding(text)

    print("Embedding length:", len(embedding))
    print("First 5 values:", embedding[:5])
