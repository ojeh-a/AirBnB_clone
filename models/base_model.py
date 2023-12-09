#!/usr/bin/python3
"""This midule contains BaseModel for AirBnB project"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    This class defines all common attributes for other classes

    Attributes:
        id(str): handles unique user identity
        ceated_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: returns the class name, id and create the dictionary
                    representations of the input values
        save(self): updates update_at attribute
        to_dict(self): Returns the dictionary representation of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        Public instance attribute constructor

        Args:
            *args: arguments
            **kwargs: attribute values
        """

        DATE_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ('updated_at', 'created_at'):
                    self.__dict__[key] = value
                elif key == 'id':
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = value
        storage.new(self)

    def __str__(self):
        """
        Returns the string representatiom of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates the update_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of the obj"""
        d = self.__dict__
        d["__class__"] = self.__class__.__name__
        return d
