import wikipedia

def fetch_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=5)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=5)
    except:
        return ""

def get_trusted_data(query):
    data = fetch_wikipedia(query)

    if data:
        return data
    else:
        return "No reliable data found."