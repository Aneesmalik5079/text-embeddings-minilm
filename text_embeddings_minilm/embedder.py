from sentence_transformers import SentenceTransformer

# Load the model once (cached automatically by Hugging Face)
_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    """
    Convert input text into a vector embedding using all-MiniLM-L6-v2.

    Args:
        text (str): Input text

    Returns:
        list: Embedding vector (length = 384)
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    embedding = _model.encode(text)
    return embedding.tolist()
