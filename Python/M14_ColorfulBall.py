from vpython import *
from random import random
Ball=sphere()
deltaX=.01
deltaY=.02
deltaZ=.03
x=random()
y=random()
z=random()
while True:
    x=x+deltaX
    y=y+deltaY
    z=z+deltaZ
    if x>.99 or x<.01:
        deltaX=deltaX*(-1)
    if y>.98 or y<.02:
        deltaY=deltaY*(-1)
    if z>.97 or z<.03:
        deltaZ=deltaZ*(-1)
    Ball.color=vec(x,y,z)
    sleep(.001)