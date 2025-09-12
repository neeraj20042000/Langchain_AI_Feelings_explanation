"""
user_input.py

Defines the Pydantic model for user input to the API.
"""

from pydantic import BaseModel

class UserInput(BaseModel):
    """
    Model for user input containing the feeling and model name.
    """
    text: str  # The feeling to explain
    model: str # The model name to use