#Spiral pattern
import turtle         
wind = turtle.Screen()
wind.bgcolor("pink") 
p = turtle.Turtle()
s = 0
while True:
  for i in range(5): 
        p.fd(s + 1)
        p.left(72)
        s = s - 5
  s = s + 1