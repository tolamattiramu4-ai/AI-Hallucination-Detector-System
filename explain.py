def explain(similarity, keyword):
    if similarity < 0.4:
        return "Low semantic similarity"
    elif keyword < 0.3:
        return "Keyword mismatch"
    else:
        return "Partial match with trusted data"