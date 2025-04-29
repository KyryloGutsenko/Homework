from abc import ABC, abstractmethod

class Schape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Schape):

    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Schape):

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def calculate_area(self):
        return self.width * self.height


class Triangle(Schape):

    def __init__(self, height, side):
        self.height = height
        self.side = side


    def calculate_area(self):
        return (self.height * self.side) / 2


circle = Circle(15)
rectangle = Rectangle(20, 8)
triangle = Triangle(20, 8)
print(circle.calculate_area(), rectangle.calculate_area(), triangle.calculate_area())