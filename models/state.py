#!/usr/bin/python3
"""state class inheriting from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class
    Attrs:
        name: (str) name of state
    """
    name = ""
