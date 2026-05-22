from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity(a, b):
    # Convert dict/list to string safely
    if isinstance(a, dict):
        a = str(a)
    if isinstance(b, dict):
        b = str(b)

    if isinstance(a, list):
        a = " ".join(map(str, a))
    if isinstance(b, list):
        b = " ".join(map(str, b))

    tfidf = TfidfVectorizer().fit_transform([a, b])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]