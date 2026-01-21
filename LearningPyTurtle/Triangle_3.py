import turtle

t = turtle.Turtle()

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

# or we use loop
for i in range(3):
  t.forward(100)
  t.left(120)
