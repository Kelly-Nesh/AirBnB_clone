#!/usr/bin/python3
"""City class inheriting from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class
    Attrs:
        name: (str) name of city
        state_id: (str) id of state city belongs to
    """
    state_id = ""
    name = ""
