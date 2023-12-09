#!/usr/bin/python3
"""Contains the FileStorage class model"""
import json


class FileStorage:
    """Serializes instances to a JSON file and
        deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary `__objects`
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """
        deserializes the JSON file to __objects if it exists
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except Exception:
            pass
