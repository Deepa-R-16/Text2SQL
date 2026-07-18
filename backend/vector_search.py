import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("faiss_index.bin")

# Load documents
with open("documents.pkl", "rb") as f:
    documents = pickle.load(f)

def search_similar(query, top_k=2):
    # Convert query to embedding
    query_embedding = model.encode([query])

    # Search similar documents
    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []
    for idx in indices[0]:
        results.append(documents[idx])

    return results