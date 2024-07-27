from vpython import *
from random import *
from threading import Thread

def move(xPos,yPos,zPos,theObject):
    deltaX=.1
    deltaY=.1
    deltaZ=.1
    while True:
        if yPos==roomHeight/2-((wallThickness/2)+ballRadius) or yPos==-(roomHeight/2)+(wallThickness/2)+ballRadius:
            deltaY=deltaY*(-1)
        if xPos==roomWidth/2-((wallThickness/2)+ballRadius) or xPos==-(roomWidth/2)+(wallThickness/2)+ballRadius:
            deltaX=deltaX*(-1)
        if zPos==roomDepth/2-((wallThickness/2)+ballRadius) or zPos==-(roomDepth/2)+(wallThickness/2)+ballRadius:
            deltaZ=deltaZ*(-1)
        xPos=round(xPos+deltaX,1)
        yPos=round(yPos+deltaY,1)
        zPos=round(zPos+deltaZ,1)
        theObject.pos=vector(xPos,yPos,zPos)
        sleep(.001)

def colour(theObject):
    while True:
        theObject.color=vec(.5,.5,1)
        sleep(2)
        theObject.color=vec(0,0,0)
        sleep(2)
        theObject.color=vec(1,0,1)
        sleep(2)
        theObject.color=vec(1,0,0)
        sleep(2)

roomDepth=100
roomHeight=100
roomWidth=100
wallThickness=3
ballRadius=5
a=color.cyan

objectX=round(uniform(-(roomWidth/2)+(wallThickness/2)+ballRadius,roomWidth/2-((wallThickness/2)+ballRadius)),1)
objectY=round(uniform(-(roomHeight/2)+(wallThickness/2)+ballRadius,roomHeight/2-((wallThickness/2)+ballRadius)),1)
objectZ=round(uniform(-(roomDepth/2)+(wallThickness/2)+ballRadius,roomDepth/2-((wallThickness/2)+ballRadius)),1)

myObject1=box(color=a, pos=vector(0,0,-roomDepth/2),length=roomWidth+wallThickness,width=wallThickness,height=roomHeight+wallThickness)
myObject2=box(color=a, pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight+wallThickness,roomDepth+wallThickness))
myObject3=box(color=a, pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight+wallThickness,roomDepth+wallThickness))
myObject4=box(color=a, pos=vector(0,-roomHeight/2,0),size=vector(roomWidth+wallThickness,wallThickness,roomDepth+wallThickness))
myObject5=box(color=a, size=vector(roomWidth+wallThickness,wallThickness,roomDepth+wallThickness),pos=vector(0,roomHeight/2,0))
myObject6=sphere(radius=ballRadius,color=color.black)

colorThread=Thread(target=colour, args=(myObject6,), daemon=True)
moveThread=Thread(target=move, args=(objectX,objectY,objectZ,myObject6), daemon=True)

colorThread.start()
moveThread.start()

while True:
    pass