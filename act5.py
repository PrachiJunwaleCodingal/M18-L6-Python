#Colorful spiral
import turtle            
col = [ "orange","purple","blue","green","yellow","black"]  
p = turtle.Pen()
turtle.bgcolor("pink") 
for x in range(360):
   p.pencolor(col[x % 6]) 
   p.width(x/100 + 2)
   p.forward(x)
   p.left(59)