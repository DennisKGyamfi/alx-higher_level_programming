#!/usr/bin/python3
"""
this module contains the rectangle subclass
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass of BasedGeometry"""
    def __init__(self, width, height):
        """a representation of a rectangle """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
