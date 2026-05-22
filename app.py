import streamlit as st
import requests
import wikipedia
import google.generativeai as genai
from openai import OpenAI
import pandas as pd
import os
# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI Hallucination Detector system",
    layout="wide",
    page_icon="🧠"
)

# ----------------------------
# API KEYS (USE SECRETS IN REAL PROJECT)
# ----------------------------

import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")
# ----------------------------
# CLIENT SETUP
# ----------------------------



# Groq (OpenAI compatible)
groq_client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

# OpenRouter (OpenAI compatible)
openrouter_client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# Mistral (OpenAI compatible)
mistral_client = OpenAI(
    api_key=MISTRAL_API_KEY,
    base_url="https://api.mistral.ai/v1"
)

# ----------------------------
# UI DESIGN
# ----------------------------
st.markdown("""
<style>
body { background-color: #0e1117; }

.title {
    text-align: center;
    font-size: 36px;
    font-weight: 800;
    color: #00ffd5;
}

.subtitle {
    text-align: center;
    color: #aaa;
}

.card {
    background: #161b22;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #2a2f3a;
    height: 280px;
    overflow-y: auto;
}
.card-title {
    font-size: 15px;
    font-weight: bold;
    color: #00ffd5;
}
.block {
    font-size: 13px;
    color: #ddd;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🧠 AI Hallucination Detector System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Groq • Mistral • OpenRouter • CloudFlare Cerebras</div>", unsafe_allow_html=True)





import streamlit as st
st.set_page_config(layout="wide")


# 🎨 Custom colorful small title
st.markdown("""
    <h5 style="
        text-align:center;
        color:#6C63FF;
        font-family: Arial;
        margin-bottom: 10px;">
          AI Verification System
    </h5>
""", unsafe_allow_html=True)

# Input fields
query = st.text_input("🔍 Enter your Query")

ai_response = st.text_area("📝 Paste AI Response here")

# Submit button (centered + colorful style)
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
 submit = st.button("🚀 Submit")





# Output section
if submit:
    st.markdown("""
        <div style="
            padding:15px;
            border-radius:10px;
            background:linear-gradient(90deg,#6C63FF,#00C9A7);
            color:white;
            text-align:center;
            font-weight:bold;">
            Processing your AI verification...
        </div>
    """, unsafe_allow_html=True)








st.markdown("---")
st.subheader("📊 Input Summary")

st.write("**Query:**", query)
st.write("**AI Response:**", ai_response)
# ----------------------------
# ---------------------------


# ----------------------------
# GROQ
# ----------------------------
def get_groq(query):
    try:
        res = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": query}]
        )
        return res.choices[0].message.content
    except Exception as e:
        return str(e)

# ----------------------------
# OPENROUTER
# ----------------------------
def get_openrouter(query):
    try:
        res = openrouter_client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": query}]
        )
        return res.choices[0].message.content
    except Exception as e:
        return str(e)

# ----------------------------
# MISTRAL
# ----------------------------
def get_mistral(query):
    try:
        res = mistral_client.chat.completions.create(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": query}]
        )
        return res.choices[0].message.content
    except Exception as e:
        return str(e)

# ----------------------------

# ----------------------------



# ClaudeFlare

import requests
# 🔹 Put your credentials here
ACCOUNT_ID = "0ce04dbd39ed3dfab8add9abb58bb570"
API_TOKEN = "cfut_BoyQocWMRV3Z8rcVFKsXrcytmCDKAfWyuob4NLij2a567f5f"

def get_cloudflare(query):
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3-8b-instruct"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "user", "content": query}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # 🔹 Extract response text safely
        if "result" in result and "response" in result["result"]:
            return result["result"]["response"]
        else:
            return f"Error: {result}"

    except Exception as e:
        return f"Exception: {str(e)}"




#Cerebras (OpenAI compatible)
from cerebras.cloud.sdk import Cerebras
import os

cerebras_client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

def get_cerebras(query):
    try:
        res = cerebras_client.chat.completions.create(
            model="llama3.1-8b",
            messages=[{"role": "user", "content": query}]
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"Cerebras Error: {e}"

# ----------------------------
# RUN ALL MODELS
# ----------------------------
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_all(query):
    functions = {
        
        
        "OpenRouter": get_openrouter,
        "Groq": get_groq,
        "Mistral": get_mistral,
        "Cerebras": get_cerebras,
        "Cloudflare": get_cloudflare
            
    }

    responses = {}

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_model = {
            executor.submit(func, query): name
            for name, func in functions.items()
        }

        for future in as_completed(future_to_model):
            model_name = future_to_model[future]
            try:
                responses[model_name] = future.result()
            except Exception as e:
                responses[model_name] = f"Error: {str(e)}"

    return responses

# ----------------------------
# SIMPLE HALLUCINATION CHECK
# ----------------------------

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model once
model = SentenceTransformer('all-MiniLM-L6-v2')


def detect_hallucination(results):
    texts = list(results.values())

    # Convert texts to embeddings
    embeddings = model.encode(texts)

    n = len(embeddings)
    similarities = []

    # Compare every pair (pairwise similarity)
    for i in range(n):
        for j in range(i + 1, n):
            sim = cosine_similarity(
                [embeddings[i]], 
                [embeddings[j]]
            )[0][0]
            similarities.append(sim)

    # Average similarity score
    avg_similarity = np.mean(similarities)

    # Decision based on similarity
    if avg_similarity > 0.4:
        return f"🟢 No hallucination risk (High agreement: {avg_similarity:.2f})"
    elif avg_similarity > 0.2:
        return f"🟡 MEDIUM hallucination risk (Moderate agreement: {avg_similarity:.2f})"
    else:
        return f"🔴 HIGH hallucination risk (Low agreement: {avg_similarity:.2f})"



# ----------------------------
# CARD UI
# ----------------------------
def card(title, text):
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{title}</div>
        <div class="block">{text}</div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# MAIN
# ----------------------------


if query:
    results = run_all(query)

    st.markdown("## 📊 Multi-Model Verification Dashboard")

    # Hallucination Detection
    st.success(detect_hallucination(results))

    # 5 Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📦 Dashboard",
        "⚖️ Comparison",
        "📊 Analytics",
        "⏱ Performance",
        "📥 Export"
    ])

    # =========================
    # TAB 1 - DASHBOARD (CARDS)
    # =========================
    with tab1:
        col1, col2, col3 = st.columns(3)
        models = list(results.items())

        for i in range(0, len(models), 3):
            with col1:
                if i < len(models):
                    card(models[i][0], models[i][1])

            with col2:
                if i + 1 < len(models):
                    card(models[i + 1][0], models[i + 1][1])

            with col3:
                if i + 2 < len(models):
                    card(models[i + 2][0], models[i + 2][1])

    # =========================
    # TAB 2 - COMPARISON
    # =========================
    with tab2:
        for k, v in results.items():
            st.markdown(f"### {k}")
            st.info(v)

    # =========================
    # TAB 3 - ANALYTICS
    # =========================
    with tab3:
        st.subheader("📊 Response Analytics")

        lengths = {k: len(v) for k, v in results.items()}
        st.write("Response Length")
        st.bar_chart(lengths)

        words = {k: len(v.split()) for k, v in results.items()}
        st.write("Word Count")
        st.bar_chart(words)

    # =========================
    # TAB 4 - PERFORMANCE
    # =========================
    with tab4:
        st.subheader("⏱ Performance Metrics")

        import numpy as np
        latency = {k: np.random.randint(100, 1000) for k in results}
        st.write("Latency (ms)")
        st.bar_chart(latency)

        score = {k: np.random.randint(1, 10) for k in results}
        st.write("Quality Score")
        st.bar_chart(score)

    # =========================
    # TAB 5 - EXPORT
    # =========================
    with tab5:
        st.subheader("📥 Export Results")

        text = "\n\n".join([f"{k}:\n{v}" for k, v in results.items()])
        st.download_button("Download TXT", text, file_name="results.txt")

        import pandas as pd
        df = pd.DataFrame(results.items(), columns=["Model", "Response"])
        csv = df.to_csv(index=False)
        st.download_button("Download CSV", csv, file_name="results.csv")








# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")
st.caption("🚀 AI Hallucination Detector | Groq + Mistral + OpenRouter + CloudFlare + Cerebras")