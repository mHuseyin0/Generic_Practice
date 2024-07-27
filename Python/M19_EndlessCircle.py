import turtle
Screen1=turtle.getcanvas()
Marker1=turtle.Turtle(shape='circle')
turtle.bgcolor('gray')
Marker1.speed(1000)
Marker1.shapesize(.5,.5,.5)
radius=1
while 'xd':
    Marker1.circle(radius=radius,extent=1)
    radius+=.1
input()