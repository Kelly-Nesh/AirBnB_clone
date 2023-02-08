#!/usr/bin/python3
import uuid
from datetime import datetime
"""Defining a BaseModel Class that defines all common
attributes/methods for other classes"""


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at =
        self.updated_at = datetime.now()
        # if first time update both created_at and updated_at
        # if second time just update updated_at


    def __str__(self):
