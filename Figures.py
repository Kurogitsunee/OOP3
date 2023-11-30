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
        return side(self.p1, self.p2) + side(self.p1, self.p3) + side(self.p3, self.p2)
    
    def square(self):
        p = self.perimeter()/2
        return sqrt(abs(p * (p - side(self.p1, self.p2)) * (p - side(self.p1, self.p3) * (p - side(self.p3, self.p2)))))
    
    def show(self):
        print(f"Triangle is built by points p1({self.p1[0]}; {self.p1[1]}), p2({self.p2[0]}; {self.p2[1]}), p3({self.p3[0]}; {self.p3[1]})")
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
        return 2 * pi * side(self.r, self.o)
    
    def square(self):
        return pi * side(self.r, self.o)**2
    
    def show(self):
        print(f"Circle with center at point o({self.o[0]}; {self.o[1]}) and radius r = {side(self.r, self.o)}")
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
        return side(self.p1, self.p2) + side(self.p1, self.p4) + side(self.p3, self.p2) + side(self.p3, self.p4)
    
    def square(self):
        return Triangle(self.p1, self.p2, self.p3).square() + Triangle(self.p1, self.p3, self.p4).square()
    
    def show(self):
        print(f"Rectangle is built by points at it's diagonal p1({self.p1[0]}; {self.p1[1]}) and p3({self.p3[0]}; {self.p3[1]}) (points at another diagonal: p2({self.p2[0]}; {self.p2[1]}), p4({self.p4[0]}; {self.p4[1]}))")
        print(f"Rectangle's perimeter P = {self.perimeter()}")
        print(f"Rectangle's square S = {self.square()}")


class Point():

    def __init__(self, x, y):
        self.__coorfinates = [x, y]

    @property
    def coordinates(self):
        return self.__coorfinates
    

n = int(input("How many figures want you to create? "))
figures = []
i = 0
while i < n:
    figure_type = input("Write type of figure (triangle, rectangle, circle): ").lower()
    match figure_type:
        case "triangle":
            point1 = Point(float(input("Write x coordinate for 1st point: ")), float(input("Write y coordinate for 1st point: ")))
            point2 = Point(float(input("Write x coordinate for 2nd point: ")), float(input("Write y coordinate for 2nd point: ")))
            point3 = Point(float(input("Write x coordinate for 3rd point: ")), float(input("Write y coordinate for 3rd point: ")))
            figures.append(Triangle(point1.coordinates, point2.coordinates, point3.coordinates))
            i += 1
        case "rectangle":
            point1 = Point(float(input("Write x coordinate for 1st point: ")), float(input("Write y coordinate for 1st point): ")))
            point2 = Point(float(input("Write x coordinate for 2nd point: ")), float(input("Write y coordinate for 2nd point: ")))
            point3 = Point(float(input("Write x coordinate for 3rd point: ")), float(input("Write y coordinate for 3rd point: ")))
            point4 = Point(float(input("Write x coordinate for 4th point: ")), float(input("Write y coordinate for 4th point: ")))
            figures.append(Rectangle(point1.coordinates, point2.coordinates,  point3.coordinates, point4.coordinates))
            i += 1
        case "circle":
            center = Point(float(input("Write x coordinate for circle's centre: ")), float(input("Write y coordinate for circle's centre: ")))
            radius = Point(float(input("Write x coordinate for point at circle's radius: ")), float(input("Write y coordinate for point at circle's radius: ")))
            figures.append(Circle(center.coordinates, radius.coordinates))
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
