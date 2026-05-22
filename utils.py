import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def keyword_overlap(text1, text2):
    words1 = set(word_tokenize(text1.lower()))
    words2 = set(word_tokenize(text2.lower()))

    common = words1.intersection(words2)

    if len(words1) == 0:
        return 0

    return len(common) / len(words1)