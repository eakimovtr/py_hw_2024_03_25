from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self) -> float:
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}. "
    
    
class Rectangle(Shape):
    
    def __init__(self, length: float, width: float):
        self.length: float = length
        self.width: float = width
    
    # Magic __int__ method will round float result of calculate_area method
    def __int__(self) -> int:
        return int(self.calculate_area())
    
    def calculate_area(self):
        return self.length * self.width
    
    def __str__(self) -> str:
        return super().__str__() + f"Length: {self.length}, width: {self.width}"
    
    
class RightTriangle(Shape):
    
    def __init__(self, leg_a: float, leg_b: float):
        self.leg_a: float = leg_a
        self.leg_b: float = leg_b
        
    # Magic __int__ method will round float result of calculate_area method
    def __int__(self) -> int:
        return int(self.calculate_area())
    
    def calculate_area(self):
        return self.leg_a * self.leg_b / 2
    
    def calculate_hypotenuse(self) -> float:
        return math.sqrt(self.leg_a ** 2 + self.leg_b ** 2)
    
    def __str__(self) -> str:
        return super().__str__() + f"Legs: {self.leg_a}, {self.leg_b}, hypotenuse: {round(self.calculate_hypotenuse(), 2)}"
    
    
class Trapezoid(Shape):
    
    def __init__(self, base_a: float, base_b: float, height: float):
        self.base_a: float = base_a
        self.base_b: float = base_b
        self.height: float = height
        
    # Magic __int__ method will round float result of calculate_area method
    def __int__(self) -> int:
        return int(self.calculate_area())
    
    def calculate_area(self):
        return (self.base_a + self.base_b) * self.height / 2
    
    def __str__(self) -> str:
        return super().__str__() + f"Bases: {self.base_a}, {self.base_b}, height: {self.height}"
    
    
print(int(Rectangle(1,2)))