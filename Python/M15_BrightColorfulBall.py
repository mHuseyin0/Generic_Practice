from vpython import *
import random
Ball=sphere(pos=vector(2,2,2),opacity=1)
brightness=2
a=random.random()
b=random.uniform(1-a,1)
c=brightness-(a+b)
deltaA=.01
deltaB=.011
theTriangle=triangle(   
        v0=vertex(pos=vector(a,0,0)),
        v1=vertex(pos=vector(0,b,0)),
        v2=vertex(pos=vector(0,0,c)))
c1=cylinder(color=color.red,radius=.05,length=10)
c2=cylinder(color=color.green,radius=.05,length=10,axis=vector(0,1,0))
c3=cylinder(color=color.blue,radius=.05,length=10,axis=vector(0,0,1))
while True:
    if a>.99 or a<.01:
        deltaA=deltaA*(-1)
    if b>.98 or b<.02:
        deltaB=deltaB*(-1)
    a=a+deltaA
    b=b+deltaB
    c=brightness-(a+b)
    Ball.color=vector(a,b,c)
    theTriangle.v0=vertex(pos=vector(a,0,0))
    theTriangle.v1=vertex(pos=vector(0,b,0))
    theTriangle.v2=vertex(pos=vector(0,0,c))
    sleep(.001)