#!/usr/bin/python3
"""creates a unique FileStorage instance for your application"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import user

mdcls = {"BaseModel": BaseModel, "User": user.User}
storage = FileStorage()
storage.reload()
