from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Knowledge base
documents = [
    "Users table contains user details.",
    "Orders table stores customer orders.",
    "Products table stores product information.",
    "Reviews table stores customer reviews.",
    "Order_items table links products with orders.",
    "Events table stores event information."
]

# Convert documents to embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(np.array(embeddings))

# Save FAISS index
faiss.write_index(index, "faiss_index.bin")

# Save documents
with open("documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("Vector Database (FAISS) created and saved successfully!")