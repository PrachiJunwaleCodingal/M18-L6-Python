#Spiral helix
import turtle 
w = turtle.Screen()
w.bgcolor("pink") 
turtle.speed(2) 
 
for i in range(50):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
 
turtle.exitonclick()
