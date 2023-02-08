#!/usr/bin/python3
import uuid
from datetime import datetime
"""Defining a BaseModel Class that defines all common
attributes/methods for other classes"""


class BaseModel:
    def __init__(self):
        """Initializes id, and created at when BaseModel is instantiated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = ''


    def __str__(self):
        """return string representation of the class name with the id and the dict"""
        return "[()] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_representation = self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated-at"] = self.updated_at.isoformat()
        return dict_representation
