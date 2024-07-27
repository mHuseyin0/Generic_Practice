from vpython import *
from numpy import *
from threading import Thread

def move1(h,r):
    while True:
        for a in linspace(h,(r/2)+.1,100):
            inCylinder1.length=a
            sleep(.1)
        for a in linspace((r/2)+.1,h,100):
            inCylinder1.length=a
            sleep(.1)
    return inCylinder1.length

def move2(h,r):
    while True:
        for a in linspace(h,(r/2)+.1,100):
            inCylinder2.length=a
            sleep(.2)
        for a in linspace((r/2)+.1,h,100):
            inCylinder2.length=a
            sleep(.2)
    return inCylinder2.length

theRadius=3
theHeigth=20

inBall1=sphere(color=vec(1,0,0),radius=theRadius,pos=vector(10,0,0))
inBall2=sphere(color=vec(1,0,0),radius=theRadius,pos=vector(-10,0,0))
outBall1=sphere(color=vec(.9,.9,.9),opacity=.1,radius=theRadius+.1,pos=vector(10,0,0))
outBall2=sphere(color=vec(.9,.9,.9),opacity=.1,radius=theRadius+.1,pos=vector(-10,0,0))

inCylinder1=cylinder(color=vec(1,0,0),radius=theRadius/2,length=theHeigth,pos=vector(10,theRadius/2,0),up=vector(-1,0,0))
inCylinder2=cylinder(color=vec(1,0,0),radius=theRadius/2,length=theHeigth,pos=vector(-10,theRadius/2,0),up=vector(-1,0,0))
outCylinder1=cylinder(color=vec(.9,.9,.9),opacity=.1,radius=(theRadius/2)+.1,length=theHeigth+.1,pos=vector(10,theRadius/2,0),up=vector(-1,0,0))
outCylinder2=cylinder(color=vec(.9,.9,.9),opacity=.1,radius=(theRadius/2)+.1,length=theHeigth+.1,pos=vector(-10,theRadius/2,0),up=vector(-1,0,0))

for a in linspace(theRadius+.1,theHeigth+.1,int(round((theHeigth-theRadius),0))):
    box(size=vector(theRadius/3,theRadius/15,.2),pos=vector(10,a,theRadius/2))

for a in linspace(theRadius+.1,theHeigth+.1,int(round((theHeigth-theRadius),0))):
    box(size=vector(theRadius/3,theRadius/15,.2),pos=vector(-10,a,theRadius/2))

theThread1=Thread(target=move1, args=(theHeigth,theRadius), daemon=True)
theThread2=Thread(target=move2, args=(theHeigth,theRadius), daemon=True)

theThread1.start()
theThread2.start()

while True:
    pass
