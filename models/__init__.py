#!/usr/bin/python3
"""creates a unique FileStorage instance for your application"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import user, amenity, state, place, review, city

mdcls = {"BaseModel": BaseModel, "User": user.User,
        "Amenity": amenity.Amenity, "State": state.State,
        "Place": place.Place, "Review": review.Review,
        "City": city.City}
storage = FileStorage()
storage.reload()
