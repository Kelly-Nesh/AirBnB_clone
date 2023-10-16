#!/usr/bin/python3
"""Engine for serializing and deserializing python objects and writing
    to a file."""
import json
import os
import models


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
         returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        classNameId = obj.__class__.__name__ + "." + obj.id
        self.__objects[classNameId] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dumpdict = {}
        for key, obj in self.__objects.items():
            dumpdict[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as js:
            dump = json.dumps(dumpdict)
            js.write(dump)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as js:
                dump = js.readline()
                if not dump:
                    return
                temp = json.loads(dump)
                for key, val in temp.items():
                    clsName = val["__class__"]
                    self.__objects[key] = models.mdcls[clsName](**val)
