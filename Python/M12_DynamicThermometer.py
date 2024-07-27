from vpython import *
from numpy import linspace, arange

theRadius=3
theHeigth=20

theBall=sphere(color=vec(1,0,0),radius=theRadius)
theBall2=sphere(color=vec(.9,.9,.9),opacity=.1,radius=theRadius+.1)

theCylinder=cylinder(color=vec(1,0,0),radius=theRadius/2,length=theHeigth,pos=vector(0,theRadius/2,0),up=vector(-1,0,0))
theCylinder2=cylinder(color=vec(.9,.9,.9),opacity=.1,radius=(theRadius/2)+.1,length=theHeigth+.1,pos=vector(0,theRadius/2,0),up=vector(-1,0,0))

for a in linspace(theRadius+.1,theHeigth+.1,int(round((theHeigth-theRadius),0))):
    box(size=vector(theRadius/3,theRadius/15,.2),pos=vector(0,a,theRadius/2))

while True:
    for a in linspace(theHeigth,(theRadius/2)+.1,100):
        theCylinder.length=a
        sleep(.1)
    for a in linspace((theRadius/2)+.1,theHeigth,100):
        theCylinder.length=a
        sleep(.1)
