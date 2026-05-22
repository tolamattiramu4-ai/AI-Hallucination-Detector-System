
import wikipedia
import requests
import re

# ---------------- CLEAN QUERY ----------------
def clean_query(query):
    remove_words = ["who is", "what is", "tell me about", "define", "explain"]
    q = query.lower()

    for w in remove_words:
        q = q.replace(w, "")

    return q.strip().title()


# ---------------- WIKIPEDIA ----------------
def fetch_wikipedia(query):
    try:
        wikipedia.set_lang("en")
        clean = clean_query(query)

        summary = wikipedia.summary(clean, sentences=4)

        return summary
    except:
        return ""


# ---------------- WIKIDATA ----------------
def fetch_wikidata(query):
    try:
        clean = clean_query(query)

        url = "https://www.wikidata.org/w/api.php"

        params = {
            "action": "wbsearchentities",
            "search": clean,
            "language": "en",
            "format": "json"
        }

        response = requests.get(url, params=params).json()

        if "search" in response and len(response["search"]) > 0:
            item = response["search"][0]
            description = item.get("description", "")
            label = item.get("label", "")

            return f"{label}: {description}"

        return ""
    except:
        return ""


# ---------------- DUCKDUCKGO ----------------
def fetch_duckduckgo(query):
    try:
        url = "https://api.duckduckgo.com/"

        params = {
            "q": query,
            "format": "json"
        }

        response = requests.get(url, params=params).json()

        abstract = response.get("AbstractText", "")
        related = response.get("RelatedTopics", [])

        extra = ""
        if related:
            for item in related[:2]:
                if "Text" in item:
                    extra += item["Text"] + " "

        return abstract + " " + extra
    except:
        return ""


# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# ---------------- MERGE ALL DATA ----------------
def get_real_world_data(query):
    wiki = fetch_wikipedia(query)
    wikidata = fetch_wikidata(query)
    duck = fetch_duckduckgo(query)

    combined = f"{wiki} {wikidata} {duck}"

    combined = clean_text(combined)

    if not combined:
        return {
            "status": "error",
            "data": "No data found"
        }

    return {
        "status": "success",
        "data": combined[:800]   # limit size
    }


# ---------------- TEST ----------------
if __name__ == "__main__":
    q = input("Enter Question: ")
    result = get_real_world_data(q)

    print("\n--- RESULT ---")
    print(result["data"])

