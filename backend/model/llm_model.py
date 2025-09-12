"""
llm_model.py

Provides a function to dynamically load a HuggingFace LLM endpoint
based on the requested model name.
"""

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def get_llm(model: str) -> ChatHuggingFace:
    """
    Returns a ChatHuggingFace instance for the specified model.

    Args:
        model (str): HuggingFace model repo_id.

    Returns:
        ChatHuggingFace: The chat model instance.
    """
    llm = HuggingFaceEndpoint(
        repo_id=model,
        task='text-generation',
        huggingfacehub_api_token=HUGGINGFACE_API_KEY,
    )
    return ChatHuggingFace(llm=llm)
