import turtle
import math

def drawCircle(t, x, y, radius):
    circumference = 2.0 * math.pi * radius
    distance = circumference / 120.0
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    for i in range(120):
        t.forward(distance)
        t.left(3)
        