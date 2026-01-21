import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")


screen.tracer(0)

t = turtle.Turtle()
t.penup()
t.hideturtle()

colors = [
    "red", "orange", "yellow", "green",
    "blue", "purple", "cyan", "white", "pink"
]

for x in range(-380, 400, 30):
    for y in range(-280, 300, 30):
        t.goto(x, y)
        t.dot(12, random.choice(colors))

# UPDATE SCREEN ONCE
screen.update()

turtle.done()
