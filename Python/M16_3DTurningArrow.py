from vpython import *
import numpy as np
length1=10
thickness1=.2
radius1=.1
a=np.pi
object1=arrow(axis=vector(1,0,0),color=color.red,length=length1,shaftwidth=thickness1)
object2=arrow(axis=vector(0,1,0),color=color.green,length=length1,shaftwidth=thickness1)
object3=arrow(axis=vector(0,0,1),color=color.blue,length=length1,shaftwidth=thickness1)
object4=arrow()
object5=sphere(radius=radius1,make_trail=True,trail_color=vec(.67,.84,.90))
while True:
    for b in np.linspace(0,2*(-a),1000):
        object4.axis=vector(np.sin(b)*length1,0,np.cos(b)*length1)
        object4.length=length1
        object4.shaftwidth=thickness1
        object5.pos=vector(np.sin(b)*length1,0,np.cos(b)*length1)
        sleep(.01)
    for b in np.linspace(0,5*(a/2),1000):
        object4.axis=vector(0,np.sin(b)*length1,np.cos(b)*length1)
        object4.length=length1
        object4.shaftwidth=thickness1
        object5.pos=vector(0,np.sin(b)*length1,np.cos(b)*length1)
        sleep(.01)
    for b in np.linspace(0,5*(a/2),1000):
        object4.axis=vector(np.sin(b)*length1,np.cos(b)*length1,0)
        object4.length=length1
        object4.shaftwidth=thickness1
        object5.pos=vector(np.sin(b)*length1,np.cos(b)*length1,0)
        sleep(.01)
    for b in np.linspace(0,a/2,1000):
        object4.axis=vector(np.cos(b)*length1,0,np.sin(b)*length1)
        object4.length=length1
        object4.shaftwidth=thickness1
        object5.pos=vector(np.cos(b)*length1,0,np.sin(b)*length1)
        sleep(.01)