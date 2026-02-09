# Text Embeddings using all-MiniLM-L6-v2

A simple Python package that converts text into vector embeddings using the
**all-MiniLM-L6-v2** model from Hugging Face.

This package accepts plain text as input and returns a numerical embedding
vector that can be used for semantic search, similarity, clustering, or ML tasks.

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/Aneesmalik5079/text-embeddings-minilm.git

## Usage
from text_embeddings_minilm import get_embedding

embedding = get_embedding("Convert this text into embeddings")
print(len(embedding))  # 384

## Model Details

- Model name: all-MiniLM-L6-v2
- Embedding dimension: 384
- Source: Hugging Face (sentence-transformers)

## License

MIT License
