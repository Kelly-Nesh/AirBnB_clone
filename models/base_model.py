#!/usr/bin/python3
"""This is a module containing the class BaseModel that defines all common
    attributes/methods for other classes.
"""

import uuid
from datetime import datetime
# from models import storage
import models


class BaseModel:
    """Defines all common attributes and methods for other classes."""
    id = ""
    created_at = ""
    updated_at = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for new instances
        or
        Re-create an instance with this dictionary representation
        from to_dict.
        """
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                    continue
                self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns a string representation of the model."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Saves the model."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        modelDict = self.__dict__.copy()
        modelDict["__class__"] = self.__class__.__name__
        modelDict["created_at"] = self.created_at.isoformat()
        modelDict["updated_at"] = self.updated_at.isoformat()
        return modelDict
