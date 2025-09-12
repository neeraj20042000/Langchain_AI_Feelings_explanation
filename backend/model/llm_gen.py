"""
llm_gen.py

Contains the function to generate a response from the LLM using the provided model.
"""

from model.template import template
from schema.response_output import parser

def llm_gen(user_feeling: str, model) -> dict:
    """
    Generates a structured explanation for a feeling using the given LLM model.

    Args:
        user_feeling (str): The feeling to explain.
        model: The LLM chat model instance.

    Returns:
        dict: Parsed response containing summary, synonyms, and antonyms.
    """
    chain = template | model | parser
    final_result = chain.invoke(user_feeling)
    return {
        "summary": final_result.summary,
        "synonyms": final_result.synonyms if final_result.synonyms else ['There are no synonyms available for the mentioned feeling at the moment.'],
        "antonyms": final_result.antonyms if final_result.antonyms else ['There are no antonyms available for the mentioned feeling at the moment.']
    }

