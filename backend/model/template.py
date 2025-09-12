"""
template.py

Defines the prompt template for the AI Explanation of Feelings project.
This template guides the LLM to generate a structured JSON response
containing a summary, synonyms, and antonyms for a given feeling.

"""

from langchain_core.prompts import PromptTemplate
from schema.response_output import parser

template = PromptTemplate(
    template = '''
    You are an emotional science and emotional psychology expert.
    You are a motivational advisor.
    Explain the {user_feeling} in simple and detailed 100 words.
    Respond ONLY with a JSON object in the following format:
    {format_instructions}                   
    ''',
    input_variables=['user_feeling'],
    partial_variables={'format_instructions':parser.get_format_instructions()},
    validate_template=True
)