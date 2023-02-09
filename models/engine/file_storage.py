#!/usr/bin/python3
import json
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
        return self.__class__.__objects

    def new(self, obj):
        """sets in __objects the obj with key object id"""
        self.all()[obj.id] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(type(self).__file_path, 'w', encoding='utf-8') as jsf:
            jsf.write(json.dumps(type(self).__objects))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        if type(self).__file_path:
            try:
                with open(type(self).__file_path, 'r', encoding='utf-8') as jsf:
                    jsf_line = jsf.readline()
            except FileNotFoundError:
                pass
            else:
                type(self).__objects = json.loads(jsf_line)
