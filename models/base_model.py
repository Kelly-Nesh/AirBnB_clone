#!/usr/bin/python3
import uuid
from datetime import datetime
"""Defining a BaseModel Class that defines all common
attributes/methods for other classes"""


class BaseModel:
    def __init__(self):
        """Initializes id, and created at when BaseModel is instantiated
        
        Args:
            self: instance of BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = ''


    def __str__(self):
        return "[()] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
