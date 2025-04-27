from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingManager:
    """
    Manages semantic embeddings for prompt memory and similarity search.
    """

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = []
        self.prompts = []

    def add_prompt(self, prompt: str):
        emb = self.model.encode(prompt)
        self.embeddings.append(emb)
        self.prompts.append(prompt)

    def find_most_similar(self, query: str) -> str:
        query_emb = self.model.encode(query)
        if not self.embeddings:
            return "No prior prompts available."

        similarities = np.inner(self.embeddings, query_emb)
        index = np.argmax(similarities)
        return self.prompts[index]
