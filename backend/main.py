"""
main.py

FastAPI entrypoint for the AI Explanation of Feelings project.
Defines endpoints for health check and LLM-based explanation generation.
"""


from fastapi import FastAPI
from schema.user_input import UserInput
from model.llm_model import get_llm
from model.llm_gen import llm_gen

app = FastAPI()

# human readable endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Explanation of Feelings API"}

# machine readable endpoint
@app.get("/health")
async def health_check():
    supported_models = [
        "meta-llama/Llama-3.3-70B-Instruct",
        "mistralai/Mistral-7B-Instruct-v0.3"
    ]
    model_status = {}
    for model_name in supported_models:
        try:
            get_llm(model_name)
            model_status[model_name] = True
        except Exception:
            model_status[model_name] = False

    return {
        "status": "ok",
        "supported_models": supported_models,
        "model_loaded": model_status
    }

# Generates explanation for a feeling using the selected model.
@app.post("/llm-gen")
async def process_data(user_input: UserInput):
    model = get_llm(user_input.model)
    result = llm_gen(user_input.text,model) 
    return {"response": result,
            "model_used": user_input.model}
