#!/usr/bin/python3
""" Class FileStorage"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance, return dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        json_str = json.dumps(new_dict)

        with open(self.__file_path, mode="w+", encoding="utf-8") as file:
            file.write(json_str)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                json_string = json.load(file)
                for key in json_string.values():
                    clas = key["__class__"]
                    self.new(eval("{}({})".format(clas, '**key')))
        except FileNotFoundError:
            pass
