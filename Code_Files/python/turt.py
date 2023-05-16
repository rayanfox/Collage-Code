import turtle
fred=turtle.Turtle()

r=int(input("Enter the radius of the circle: "))
col=input("Enter the name of a color: ")
fred.fillcolor(col)
fred.begin_fill()
fred.circle(r)
fred.end_fill()
turtle.done()