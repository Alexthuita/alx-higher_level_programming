#!/usr/bin/python3
"""This student class defines a student"""


class Student:
    """illustrates a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets a dictionary representation of
        Student instance"""
        return self.__dict__

