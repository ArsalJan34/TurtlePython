import turtle

t = turtle.Turtle()

for i in range(6):
  for j in range(4):
    t.forward(80)
    t.right(90)
  t.right(60)

turtle.done()
