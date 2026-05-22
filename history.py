import streamlit as st

def save_history(query, response, score):
    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({
        "query": query,
        "response": response,
        "score": score
    })