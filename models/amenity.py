#!/usr/bin/python3
"""amenity class inheriting from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class
    Attrs:
        name: (str) name of amenity
    """
    name = ""
