import turtle
import random

class Petal:
    def __init__(self, t):
        self.t = t

    def draw(self, x, y, start_angle, petal_angle, color):
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(start_angle + petal_angle)
        self.t.pendown()
        self.t.pensize(1)
        self.t.pencolor('black')
        self.t.fillcolor(color)
        self.t.begin_fill()
        self.t.circle(30, 80)
        self.t.left(100)
        self.t.circle(30, 80)
        self.t.end_fill()
        self.t.penup()


class Stem:
    def __init__(self, t):
        self.t = t

    def draw(self, x, y, angle, length):
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(angle)
        self.t.pendown()
        self.t.pensize(3)
        self.t.pencolor("green")
        self.t.forward(length)
        self.t.penup()
        return self.t.position()

class Leaf:
    def __init__(self, t):
        self.t = t

    def draw(self, x, y, angle, distance):
        self.t.penup()
        self.t.goto(x, y)
        self.t.forward(distance/2)
        self.t.setheading(angle)
        self.t.pendown()
        self.t.pensize(1)
        self.t.fillcolor("green")
        self.t.pencolor("black")
        self.t.begin_fill()
        self.t.circle(30, 80)
        self.t.left(100)
        self.t.circle(30, 80)
        self.t.end_fill()
        self.t.penup()
class Flower:
    def __init__(self, t, num_petals, color):
        self.t = t
        self.color = color
        self.stem = Stem(t)
        self.Leaf = Leaf(t)
        self.petals = [Petal(t) for i in range(num_petals)]

    def draw(self, x, y, angle):
        rand_dist = random.randint(150,220)
        top_x, top_y = self.stem.draw(x, y, angle, rand_dist)
        self.Leaf.draw(x, y, angle, rand_dist)
        num = len(self.petals)
        for i, petal in enumerate(self.petals):
            petal.draw(top_x, top_y, angle, i * (360 / num), self.color)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def draw(self, x, y):
        start_angle = 30
        end_angle = 150
        step = (end_angle - start_angle) / (len(self.flowers) - 1) if len(self.flowers) > 1 else 0

        for i, flower in enumerate(self.flowers):
            current_angle = start_angle + (i * step)
            offset = i * 20 - (len(self.flowers) * 5)
            flower.draw(x + offset, y, current_angle)


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

flowers = [
    Flower(t, 5, "red"),
    Flower(t, 10, "orange"),
    Flower(t, 6, "purple"),
    Flower(t, 15, "pink"),
    Flower(t, 7, "yellow")
]

bouquet = Bouquet(flowers)
bouquet.draw(0, -200)

t.hideturtle()
screen.exitonclick()
 