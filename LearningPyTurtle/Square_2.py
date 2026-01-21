import turtle

t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
# or we can also use loop to draw an square
for i in range(4):
  t.forward(100)
  t.right(90)
