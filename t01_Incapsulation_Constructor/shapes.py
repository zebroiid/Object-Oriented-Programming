import math

class Triangle:
    def __init__(self, a, b, c):
        if a + b < c or b + c < a or a + c < b:
            raise ValueError
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        if self.a == self.b: return 0
        term = ((self.b - self.a) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.b - self.a))
        h = math.sqrt(max(0, self.c ** 2 - term ** 2))
        return ((self.a + self.b) / 2) * h


class Parallelogram:
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * (self.r ** 2)


def process_shapes(filename):
    shapes = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts: continue

            name = parts[0]
            params = list(map(float, parts[1:]))
            try:
                if name == "Triangle":
                    shapes.append(Triangle(*params))
                elif name == "Rectangle":
                    shapes.append(Rectangle(*params))
                elif name == "Trapeze":
                    shapes.append(Trapeze(*params))
                elif name == "Parallelogram":
                    shapes.append(Parallelogram(*params))
                elif name == "Circle":
                    shapes.append(Circle(*params))


                max_area_shape = max(shapes, key=lambda s: s.area())
                max_perimeter_shape = max(shapes, key=lambda s: s.perimeter())
            except ValueError:
                continue

    print(f"Результати для {filename}")
    print(f"Найбільша площа у фігури: {max_area_shape}, = {max_area_shape.area()} ")
    print(f"Найбільший периметр: {max_perimeter_shape}, = {max_area_shape.perimeter()}\n")



for i in range(1, 4):
    process_shapes(f"input{i:02d}.txt")