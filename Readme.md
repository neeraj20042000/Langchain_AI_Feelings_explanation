# AI Explanation of Feelings

## Overview

**AI Explanation of Feelings** is a web application that uses Large Language Models (LLMs) to provide detailed, human-friendly explanations of emotions or feelings entered by users. The app features a visually appealing Streamlit frontend and a FastAPI backend that supports dynamic model selection (e.g., Llama, Mistral). Users can choose which AI model to use for their query and receive a summary, synonyms, and antonyms for the feeling they enter.

---

## Features

- **Interactive Streamlit Frontend:**  
  Clean, responsive UI for entering feelings and viewing AI-generated explanations.
- **Dynamic Model Selection:**  
  Users can choose between supported LLMs (e.g., Llama, Mistral) for each query.
- **FastAPI Backend:**  
  Handles requests, dynamically loads the selected model, and returns structured responses.
- **Structured Output:**  
  Each response includes a summary, synonyms, and antonyms for the entered feeling.
- **Health Endpoint:**  
  `/health` endpoint reports available models and their status.
- **Disclaimer Section:**  
  Clearly informs users about the limitations and intended use of the app.

---

## Project Structure

```
AI-feelings-explanation/
│
├── backend/
│   ├── main.py                # FastAPI app with endpoints
│   ├── model/
│   │   ├── llm_model.py       # Dynamic LLM loader
│   │   ├── llm_gen.py         # LLM generation logic
│   │   ├── template.py        # Prompt template for LLM
│   ├── schema/
│   │   ├── user_input.py      # Pydantic model for input
│   │   ├── response_output.py # Pydantic model for output
│
├── frontend/
│   ├── app.py                 # Streamlit app
│
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

---

## How It Works

### 1. User Interaction

- The user enters a feeling (e.g., "love", "anxiety") in the Streamlit app.
- The user selects which AI model to use (Llama or Mistral).

### 2. Request Flow

- The frontend sends a POST request to the FastAPI backend (`/llm-gen`) with the feeling and selected model.
- The backend dynamically loads the requested model and generates a response using a carefully crafted prompt.
- The response is parsed and returned as a structured JSON object containing:
  - `summary`: A concise explanation of the feeling.
  - `synonyms`: Related words.
  - `antonyms`: Opposite words.

### 3. Display

- The frontend displays the summary, synonyms, and antonyms in separate columns for easy reading.

---

## API Endpoints

### `/llm-gen` (POST)

- **Description:** Generate explanation for a feeling using the selected model.
- **Request Body:**
  ```json
  {
    "text": "love",
    "model": "meta-llama/Llama-3.3-70B-Instruct"
  }
  ```
- **Response:**
  ```json
  {
    "response": {
      "summary": "...",
      "synonyms": ["affection", "adoration"],
      "antonyms": ["hatred", "indifference"]
    },
    "model_used": "meta-llama/Llama-3.3-70B-Instruct"
  }
  ```

### `/health` (GET)

- **Description:** Returns status and availability of supported models.
- **Response:**
  ```json
  {
    "status": "ok",
    "supported_models": [
      "meta-llama/Llama-3.3-70B-Instruct",
      "mistralai/Mistral-7B-Instruct-v0.3"
    ],
    "model_loaded": {
      "meta-llama/Llama-3.3-70B-Instruct": true,
      "mistralai/Mistral-7B-Instruct-v0.3": true
    }
  }
  ```

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/neeraj20042000/Langchain_AI_Feelings_explanation.git
cd Langchain_AI_Feelings_explanation
```

### 2. Install Dependencies

Create a virtual environment and install requirements:

```sh
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file in the `backend` directory with your HuggingFace API key:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

### 4. Run the Backend

```sh
cd backend
uvicorn main:app --reload
```

### 5. Run the Frontend

```sh
cd frontend
streamlit run app.py
```

---

## Customization

- **Add More Models:**  
  Update the `supported_models` list in `main.py` and ensure your API key has access.
- **Change Prompt:**  
  Edit `template.py` to modify how the LLM is instructed.
- **Improve Output Parsing:**  
  Adjust the Pydantic models in `schema/response_output.py` for more fields.

---

## Troubleshooting

- **Model Loading Errors:**  
  Ensure model names are correct and your API key has access.
- **Output Parsing Errors:**  
  Make sure the prompt instructs the LLM to reply in the exact JSON format expected by the parser.
- **Connection Issues:**  
  Verify backend is running and `BACKEND_URL` is set correctly in the frontend.

---

## Disclaimer

This application uses AI LLM models and is provided for testing purposes only.  
The system may occasionally generate incorrect, incomplete, or outdated information, and some features may not function as expected.  
Do not rely on it for professional advice (such as medical, legal, or financial matters).  
Always verify important details independently, and avoid sharing sensitive or personal information.

---

## Credits

- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://python.langchain.com/)
- [HuggingFace](https://huggingface.co/)
- **Model Providers:**
  - [Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3-3-70B-Instruct) by Meta
  - [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) by Mistral AI