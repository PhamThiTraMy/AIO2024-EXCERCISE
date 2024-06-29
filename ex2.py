from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def compute_area(self):
        return self.__side*self.__side

square = Square(5)
print(square.compute_area())