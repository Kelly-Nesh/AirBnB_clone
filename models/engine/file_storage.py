#!/usr/bin/python3
import json
import models
import os
"""Serializing and deserializing a class. Saving json to file"""


class FileStorage:
    """Class for Serializing and deserializing json files

    Attrs:
        __file_path: (str). path to the JSON file
        __objects: (dictionary). store all objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key object id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(type(self).__file_path, 'w', encoding='utf-8') as jsf:
            jsf.write(json.dumps(objects_dict))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        if FileStorage.__file_path:
            try:
                with open(type(self).__file_path, 'r', encoding='utf-8') as jsf:
                    try:
                        FileStorage.__objects = json.load(jsf)
                    except json.decoder.JSONDecodeError:
                        os.remove(FileStorage.__file_path)
                        return
            except FileNotFoundError:
                pass
            else:
                for key, val in FileStorage.__objects.items():
                    class_name = val["__class__"]
                    class_name = models.classes[class_name]
                    FileStorage.__objects[key] = class_name(**val)
