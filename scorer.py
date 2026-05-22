def keyword_overlap(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    return len(words1 & words2) / max(len(words1), 1)

def hybrid_score(similarity, keyword):
    return (0.7 * similarity) + (0.3 * keyword)

def decision(score):
    if score > 0.4:
        return "✅ Highly Reliable"
    elif score > 0.2:
        return "⚠️ Needs Verification"
    else:
        return "❌ Likely Hallucinated"