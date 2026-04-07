import math

class figures:
    def dimension(self):
        return None
    def square(self):
        return None
    def perimetr(self):
        return None
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        raise NotImplementedError()


class Triangle(figures):
    def __init__(self,a,b,c):
        if not self._is_valid(a, b, c):
            raise ValueError("Трикутник не існує")

        self.a = a
        self.b = b
        self.c = c
    def square(self):
        p = 0.5*self.perimeter()
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
    def perimeter(self):
            return self.a+self.b+self.c
    def _is_valid(self, a, b, c):
        return a + b > c and a + c > b and b + c > a
    def dimension(self):
        return 2
    def volume(self):
        return self.square()

class Rectangle(figures):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def square(self):
        if self.dimension() == 2:
            return self.a*self.b
        else:
            return None
    def perimeter(self):
        if self.dimension() == 2:
            return 2*(self.a+self.b)
        else:
            return None
    def dimension(self):
        return 2
    def volume(self):
        return self.square()

class Circle(figures):
    def __init__(self,r):
        self.r = r
    def square(self):
        if self.dimension() == 2:
            return math.pi*self.r**2
        else:
            return None
    def perimeter(self):
        if self.dimension() == 2:
            return 2*math.pi*self.r
        else:
            return None
    def dimension(self):
        return 2
    def volume(self):
        return self.square()

class Ball(figures):
    def __init__(self,r):
        self.r = r
    def squareSurface(self):
        return 4*math.pi*self.r**2
    def perimeter(self):
        return 2*math.pi*self.r
    def dimension(self):
        return 3
    def volume(self):
        return (4/3)*math.pi*self.r**3

class Parallelogram(figures):
    def __init__(self,a,b,h):
        self.a = a
        self.b = b
        self.h = h
    def square(self):
        return self.a*self.h
    def perimeter(self):
        return 2*(self.a+self.b)
    def dimension(self):
        return 2
    def volume(self):
        return self.square()


class Trapeze(figures):
    def __init__(self, a, b, c, d):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            raise ValueError("Invalid trapeze sides")
        self.a, self.b = a, b
        self.c, self.d = c, d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        if self.a == self.b:
            return 0
        diff = abs(self.a - self.b)
        numerator = (self.c ** 2 + diff ** 2 - self.d ** 2)
        h_squared = self.c ** 2 - (numerator / (2 * diff)) ** 2
        h = math.sqrt(max(0, h_squared))
        return ((self.a + self.b) / 2) * h
    def dimension(self):
        return 2
    def volume(self):
        return self.square()

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h
    def dimension(self):
        return 3
    def height(self):
        return self.h
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        l = math.sqrt(self.h**2 + (self.a / (2 * math.sqrt(3)))**2)
        side_triangle = (self.a * l) / 2
        return self.squareBase() + 3 * side_triangle
    def volume(self):
        return (1/3) * self.squareBase() * self.h

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def dimension(self):
        return 3
    def height(self):
        return self.h
    def squareBase(self):
        return self.a * self.b
    def squareSurface(self):
        l1 = math.sqrt(self.h**2 + (self.b/2)**2)
        l2 = math.sqrt(self.h**2 + (self.a/2)**2)

        side1 = self.a * l1
        side2 = self.b * l2

        return self.squareBase() + side1 + side2
    def volume(self):
        return (1/3) * self.squareBase() * self.h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimension(self):
        return 3

    def height(self):
        return self.h

    def squareBase(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(abs(p * (p - self.a) * (p - self.b) * (p - self.c)))

    def squareSurface(self):
        return 2 * self.squareBase() + self.perimeter() * self.h

    def volume(self):
        return self.squareBase() * self.h

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self):
        return 3

    def height(self):
        return self.c

    def squareBase(self):
        return self.a * self.b

    def squareSurface(self):
        return 2 * (self.a*self.b + self.a*self.c + self.b*self.c)

    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h
    def dimension(self):
        return 3
    def height(self):
        return self.h
    def squareBase(self):
        return math.pi * self.r ** 2
    def squareSurface(self):
        l = math.sqrt(self.r **2 + self.h**2)
        return math.pi * self.r * (self.r + l)
    def volume(self):
        return (1/3) * math.pi * self.r**2 * self.h


def create_figure(line):
    parts = line.split()
    name = parts[0]
    nums = list(map(float, parts[1:]))
    try:
        if name == "Triangle":
            return Triangle(*nums)
        elif name == "Rectangle":
            return Rectangle(*nums)
        elif name == "Circle":
            return Circle(*nums)
        elif name == "Ball":
            return Ball(*nums)
        elif name == "Parallelogram":
            return Parallelogram(*nums)
        elif name == "Trapeze":
            return Trapeze(*nums)
        elif name == "TriangularPyramid":
            return TriangularPyramid(*nums)
        elif name == "TriangularPrism":
            return TriangularPrism(*nums)
        elif name == "QuadrangularPyramid":
            return QuadrangularPyramid(*nums)
        elif name == "RectangularParallelepiped":
            return RectangularParallelepiped(*nums)
        elif name == "Cone":
            return Cone(*nums)
        else:
            return None
    except ValueError:
        return None

def find_max_figure(filename):
    figures = []

    with open(filename, "r") as f:
        for line in f:
            fig = create_figure(line)
            if fig:
                figures.append(fig)

    max_fig = max(figures, key=lambda f: f.volume())

    return max_fig