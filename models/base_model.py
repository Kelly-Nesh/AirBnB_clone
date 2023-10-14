#!/usr/bin/python3
import uuid
from datetime import datetime

"""This is a module containing the class BaseModel that defines all common
    attributes/methods for other classes."""


class BaseModel:
    """Defines all common attributes and methods for other classes."""
    id = ""
    created_at = ""
    updated_at = ""

    def __init__(self):
        """Initializes attributes for new instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self) -> str:
        """Returns a string representation of the model."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Saves the model."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        modelDict = self.__dict__
        modelDict["__class__"] = self.__class__.__name__
        modelDict["created_at"] = self.created_at.isoformat()
        modelDict["updated_at"] = self.updated_at.isoformat()
        return modelDict
