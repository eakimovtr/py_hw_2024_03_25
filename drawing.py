from abc import ABC, abstractmethod, abstractstaticmethod
import re

class Shape(ABC):
    
    # show method will print info about the figure
    @abstractmethod
    def show(self) -> None:
        pass
    
    # save method will write figure's parameters to a given file
    @abstractmethod
    def save(self, filepath: str) -> None:
        pass
    
    # Static load method will read figures from a given file and return a list of obtained figures
    def load(filepath: str) -> list:
        f = open(filepath, "r")
        lines: list[str] = []
        while True:
            line: str = f.readline()
            # if line is None then it means we reached the end of the file
            if not line:
                break
            # we check if line is really representing information about a figure in form of {Name: param, param, ...}
            elif not re.match("\\D+,\\d+", line):
                continue
            lines.append(line.split(","))
            
        figures = []
        for line in lines:
            figure_name: str = line[0]
            match figure_name:
                case "Square":
                    figures.append(Square(line[1],line[2],line[3]))
                case "Rectangle":
                    figures.append(Rectangle(line[1],line[2],line[3],line[4]))
                case "Circle":
                    figures.append(Circle(line[1],line[2],line[3]))
                case "Ellipse":
                    figures.append(Ellipse(line[1],line[2],line[3],line[4]))
                case _:
                    continue
                    
        return figures
            
        
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"
    
    
class Square(Shape):
    def __init__(self, x: float, y: float, side: float):
        self.x: float = x
        self.y: float = y
        self.side: float = side
        
    def show(self):
        print(f"Square. Side length: {self.side}. Left upper corner coordinates: {self.x}, {self.y}")
        
    def save(self, filepath: str):
        f = open(filepath, "a")
        f.write(f"Square,{self.x},{self.y},{self.side}\n")
        f.close()
    
    def __repr__(self) -> str:
        return super().__repr__() + f"({self.side}, ({self.x},{self.y}))"
    

class Rectangle(Shape):
    def __init__(self, x: float, y: float, length: float, width: float):
        self.x: float = x
        self.y: float = y
        self.length: float = length
        self.width: float = width
        
    def show(self):
        print(f"Rectangle. Length: {self.length}, width: {self.width}. Left upper corner coordinates: {self.x}, {self.y}")
        
    def save(self, filepath: str):
        f = open(filepath, "a")
        f.write(f"Rectangle,{self.x},{self.y},{self.length},{self.width}\n")
        f.close()
        
    def __repr__(self) -> str:
        return super().__repr__() + f"({self.length}, {self.width}, ({self.x},{self.y}))"
    

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float):
        self.x: float = x
        self.y: float = y
        self.radius: float = radius
        
    def show(self):
        print(f"Circle. Radius: {self.radius}. Center coordinates: {self.x}, {self.y}")
        
    def save(self, filepath: str):
        f = open(filepath, "a")
        f.write(f"Circle,{self.x},{self.y},{self.radius}\n")
        f.close()
        
    def __repr__(self) -> str:
        return super().__repr__() + f"({self.radius}, ({self.x},{self.y}))"


class Ellipse(Shape):
    def __init__(self, x: float, y: float, major: float, minor: float):
        self.x: float = x
        self.y: float = y
        self.major: float = major
        self.minor: float = minor
        
    def show(self):
        print(f"Ellipse. Major axis: {self.major}, minor axis: {self.minor}. Left upper corner coordinates: {self.x}, {self.y}")
        
    def save(self, filepath: str):
        f = open(filepath, "a")
        f.write(f"Ellipse,{self.x},{self.y},{self.major},{self.minor}\n")
        f.close()
        
    def __repr__(self) -> str:
        return super().__repr__() + f"({self.major}, {self.minor}, ({self.x},{self.y}))"
    
    
Square(1,1,4).save("figures.txt")
Rectangle(2,2,3,4).save("figures.txt")
Circle(3,3,9).save("figures.txt")
Ellipse(4,4,15,10).save("figures.txt")

shapes = Shape.load("figures.txt")
for shape in shapes:
    shape.show()