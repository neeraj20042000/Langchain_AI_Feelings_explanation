"""
response_output.py

Defines the Pydantic model and output parser for the LLM response.
"""


from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Optional

class Feeling(BaseModel):    
    summary : str = Field(description='Summary of the feeling')
    synonyms: Optional[list[str]] = Field(default=None, description='synonyms of feeling')
    antonyms: Optional[list[str]] = Field(default=None, description='antonyms of feeling')   

parser = PydanticOutputParser(pydantic_object=Feeling)