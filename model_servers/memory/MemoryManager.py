import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

class MemoryManager:
    def __init__(self, memory_dir="./model_services/memory", embedding_model="all-MiniLM-L6-v2"):
        self.memory_dir = memory_dir
        os.makedirs(self.memory_dir, exist_ok=True)

        self.index_file = os.path.join(self.memory_dir, "memory.index")
        self.data_file = os.path.join(self.memory_dir, "memory.pkl")

        self.model = SentenceTransformer(embedding_model)

        if os.path.exists(self.index_file) and os.path.exists(self.data_file):
            self.index = faiss.read_index(self.index_file)
            with open(self.data_file, "rb") as f:
                self.texts = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(384)  # 384 dims for MiniLM
            self.texts = []

    def save_memory(self):
        faiss.write_index(self.index, self.index_file)
        with open(self.data_file, "wb") as f:
            pickle.dump(self.texts, f)

    def add_memory(self, text):
        vector = self.model.encode([text])
        self.index.add(np.array(vector).astype(np.float32))
        self.texts.append(text)
        self.save_memory()

    def search_memory(self, query, top_k=3):
        if self.index.ntotal == 0:
            return []
        vector = self.model.encode([query])
        D, I = self.index.search(np.array(vector).astype(np.float32), top_k)
        results = [self.texts[i] for i in I[0] if i != -1]
        return results
