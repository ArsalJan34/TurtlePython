import turtle

t= turtle.Turtle()
size = 20

for i in range(100):
  t.forward(size)
  t.right(90)
  size+= 5
turtle.done()
