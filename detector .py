

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class Detector:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def similarity(self, text1, text2):
        emb1 = self.model.encode([text1])
        emb2 = self.model.encode([text2])
        return cosine_similarity(emb1, emb2)[0][0]
    
