import turtle

t = turtle.Turtle()
colors = ["red", "green", "blue", "orange", "violet"]
for i in range(36):
  t.color(colors[i % 5])
  t.circle(100)
  t.right(10)
turtle.done()
