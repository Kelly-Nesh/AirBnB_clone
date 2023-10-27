#!/usr/bin/python3
"""review class inheriting from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    Attrs:
        text: (tr)
    """
    place_id = ""
    user_id = ""
    text = ""
