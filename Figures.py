from abc import ABCMeta, abstractmethod, abstractproperty
from math import pi as pi
from math import sqrt as sqrt

def side(p1=[0,0], p2=[0,0]):
    return sqrt((p2[0]-p1[0])**2 + ((p2[1]-p1[1])**2))

class Figure():

    __meta_class__ = ABCMeta

    @abstractmethod
    def perimeter():
        """Calculate perimeter"""
    
    @abstractmethod
    def square():
        """Calculate square"""

    @abstractmethod
    def show():
        """Print figure"""

    
class Triangle(Figure):

    def __init__(self, p1, p2, p3):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3

    @property
    def p1(self):
        return self.__p1
    
    @property
    def p2(self):
        return self.__p2
    
    @property
    def p3(self):
        return self.__p3
    
    def perimeter(self):
        return side(self.p1.coordinates, self.p2.coordinates) + side(self.p1.coordinates, self.p3.coordinates) + side(self.p3.coordinates, self.p2.coordinates)
    
    def square(self):
        p = self.perimeter()/2
        return sqrt(abs(p * (p - side(self.p1.coordinates, self.p2.coordinates)) * (p - side(self.p1.coordinates, self.p3.coordinates) * (p - side(self.p3.coordinates, self.p2.coordinates)))))
    
    def show(self):
        print(f"Triangle is built by points p1{self.p1}, p2{self.p2}, p3{self.p3}")
        print(f"Triangle's perimeter P = {self.perimeter()}")
        print(f"Triangle's square S = {self.square()}")


class Circle(Figure):

    def __init__(self, o, r):
        self.__o = o  # circle's center
        self.__r = r  # point at circle's radius

    @property
    def o(self):
        return self.__o
    
    @property
    def r(self):
        return self.__r
    
    def perimeter(self):
        return 2 * pi * side(self.r.coordinates, self.o.coordinates)
    
    def square(self):
        return pi * side(self.r.coordinates, self.o.coordinates)**2
    
    def show(self):
        print(f"Circle with center at point o{self.o} and radius r = {side(self.r.coordinates, self.o.coordinates)}")
        print(f"Circle's perimeter P = {self.perimeter()}")
        print(f"Circle's square S = {self.square()}")


class Rectangle(Figure):

    def __init__(self, p1, p2, p3, p4):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__p4 = p4

    @property
    def p1(self):
        return self.__p1
    
    @property
    def p2(self):
        return self.__p2
    
    @property
    def p3(self):
        return self.__p3
    
    @property
    def p4(self):
        return self.__p4
    
    def perimeter(self):
        return side(self.p1.coordinates, self.p2.coordinates) + side(self.p1.coordinates, self.p4.coordinates) + side(self.p3.coordinates, self.p2.coordinates) + side(self.p3.coordinates, self.p4.coordinates)
    
    def square(self):
        return Triangle(self.p1, self.p2, self.p3).square() + Triangle(self.p1, self.p3, self.p4).square()
    
    def show(self):
        print(f"Rectangle is built by points at it's diagonal p1{self.p1} and p3{self.p3} (points at another diagonal: p2{self.p2}, p4{self.p4})")
        print(f"Rectangle's perimeter P = {self.perimeter()}")
        print(f"Rectangle's square S = {self.square()}")


class Point():

    def __init__(self):
        self.__coordinates = [float(input("Write x coordinate: ")), float(input("Write y coordinate: "))]

    @property
    def coordinates(self):
        return self.__coordinates
    
    def __str__(self) -> str:
        return f"({self.coordinates[0]}; {self.coordinates[1]})"
    

n = int(input("How many figures want you to create? "))
figures = []
i = 0
while i < n:
    figure_type = input("Write type of figure (triangle, rectangle, circle): ").lower()
    match figure_type:
        case "triangle":
            print("1st point")
            point1 = Point()
            print("2nd point")
            point2 = Point()
            print("3rd point")
            point3 = Point()
            figures.append(Triangle(point1, point2, point3))
            i += 1
        case "rectangle":
            print("1st point")
            point1 = Point()
            print("2nd point")
            point2 = Point()
            print("3rd point")
            point3 = Point()
            print("4th point")
            point4 = Point()
            figures.append(Rectangle(point1, point2,  point3, point4))
            i += 1
        case "circle":
            print("Circle's centre")
            center = Point()
            print("Point at circle's radius")
            radius = Point()
            figures.append(Circle(center, radius))
            i += 1
        case default:
            print("Unknown figure")

print("-"*20)

for j in range(n):
    for k in range(j+1, n):
        if figures[k].square() < figures[j].square():
            figures[k], figures[j] = figures[j], figures[k]

for figure in figures:
    figure.show()
    print("-"*20)
