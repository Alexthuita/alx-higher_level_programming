#!/usr/bin/python3
"""A Student class defines a student"""


class Student:
    """illustrates a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets a dictionary representation of
        Student instance"""
        if type(attrs) == list and all(type(elem) == str for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """this replaces all attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)


