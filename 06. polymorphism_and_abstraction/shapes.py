from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_area(self):
        return pi * pow(self.__radius, 2)

    def calculate_perimeter(self):
        return pi * (2 * self.__radius)


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


circle = Circle(5)
print(f"Circle area: {circle.calculate_area()}")
print(f"Circle perimeter: {circle.calculate_perimeter()}")
print()

rectangle = Rectangle(10, 20)
print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Rectangle perimeter: {rectangle.calculate_perimeter()}")
