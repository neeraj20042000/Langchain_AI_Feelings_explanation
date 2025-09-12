"""
app.py

Streamlit frontend for the AI Explanation of Feelings project.
Allows users to enter a feeling, select an AI model, and view
an AI-generated explanation including summary, synonyms, and antonyms.

Usage:
    Run with: streamlit run app.py
"""

import streamlit as st
import requests
import os

# Backend API endpoint
BACKEND_URL = "127.0.0.1:8000/llm-gen"

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Explanation of Feelings",
    page_icon="✨",
    layout="wide",
)

# -------------------------------
# Page Layout
# -------------------------------

col_left, col_center, col_right = st.columns([1,3,1])

with col_center:
    st.markdown("<h2 style='text-align: center;'>AI Explanation of Feelings</h2>", unsafe_allow_html=True)
    user_feeling = st.text_input("", placeholder="Enter your feelings here...", key="input", label_visibility="collapsed")

    c1, c2, c3, c4 = st.columns([1,1,1,1])
    with c2:
        llama = st.button("Ask Llama AI")           
    with c3:
        mistral = st.button("Ask Mistral AI")

    st.write("####")  # Spacer

model = 'meta-llama/Llama-3.3-70B-Instruct' if llama else 'mistralai/Mistral-7B-Instruct-v0.3'

# -------------------------------
# Interaction with Backend            
if model and user_feeling.strip():
    with st.spinner(f"Generating... from {model}"):
        try:
            response = requests.post(
                BACKEND_URL,
                json={
                    "text": user_feeling.strip(),
                    "model": model
                }
            )
            if response.status_code == 200:
                result = response.json().get("response", "")
                summary = result.get("summary", "No summary available.")
                synonyms = result.get("synonyms", [])
                antonyms = result.get("antonyms", [])
                model = response.json().get("model_used", "")
                with col_center:
                    st.markdown(f"<h6 style='text-align: center;'>LLM model: {model}</h4>", unsafe_allow_html=True)
                    st.markdown("<h3 style='text-align: center;'>Explanation</h3>",unsafe_allow_html=True)
                    st.text_area("Center Box", value=summary, height=100, label_visibility="collapsed")                                                   
                with col_left:
                    st.markdown("<h3 style='text-align: center;'>Synonyms</h3>",unsafe_allow_html=True)
                    st.text_area("Left Box", value=("\n".join([f"• {word}" for word in synonyms])), height=200, label_visibility="collapsed")     
                with col_right:
                    st.markdown("<h3 style='text-align: center;'>Antonyms</h3>",unsafe_allow_html=True)
                    st.text_area("Right Box", value=("\n".join([f"• {word}" for word in antonyms])), height=200, label_visibility="collapsed")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to FastAPI: {e}")   
else:
    st.warning("Please enter some text and select a model.")    

# -------------------------------
# Disclaimer Section
# -------------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 13px; color: gray;'>
    <b>Disclaimer:</b> This application uses AI LLM models and is provided for testing purposes only.  
    The system may occasionally generate incorrect, incomplete, or outdated information, and some features may not function as expected.  
    Do not rely on it for professional advice (such as medical, legal, or financial matters).  
    Always verify important details independently, and avoid sharing sensitive or personal information.  
    </div>
    """,
    unsafe_allow_html=True
)