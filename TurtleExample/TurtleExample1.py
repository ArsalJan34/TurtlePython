import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Practice")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Draw spiral squares
size = 20
for i in range(60):
    t.color(colors[i % len(colors)])
    draw_square(size)
    t.right(10)
    size += 5

turtle.done()
