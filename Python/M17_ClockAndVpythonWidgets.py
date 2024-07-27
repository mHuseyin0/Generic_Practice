# May not work properly on Linux due to vpython
from vpython import *
import numpy as np
import time

def changeBackground(x):
    if x.checked==True:
        theClock.color=vec(.2,.2,.2)
    if x.checked==False:
        theClock.color=vec(.3,.3,.3)

def changeHandColor(x):
    if x.checked==True:
        theCenter.color=color.red
        theHourHand.color=color.red
        theMinuteHand.color=vec(.3,.4,.72)
        theSecondHand.color=vec(.6,.8,.6)
    if x.checked==False:
        theCenter.color=color.red
        theHourHand.color=color.red
        theMinuteHand.color=vec(.5,.5,.8)
        theSecondHand.color=color.white

def correctionTime(x):
    global i
    global b
    theTime=time.localtime(time.time())
    theHour=theTime.tm_hour
    theMinute=theTime.tm_min
    theSecond=theTime.tm_sec
    i=b*(theHour*3600+theMinute*60+theSecond)

def redLabel(x):
    global Lred
    Lred=x.value

def greenLabel(x):
    global Lgreen
    Lgreen=x.value

def blueLabel(x):
    global Lblue
    Lblue=x.value

def secondOption(x):
    global secondOpacity
    global b
    global i
    if x.selected=='Classic':
        b=1
        i=b*(theHour*3600+theMinute*60+theSecond)
        secondOpacity=1
    if x.selected=='Smooth':
        b=25
        i=b*(theHour*3600+theMinute*60+theSecond)
        secondOpacity=1
    if x.selected=='Closed':
        secondOpacity=0
        b=1
        i=b*(theHour*3600+theMinute*60+theSecond)
    
lengthM=5
u=lengthM/15
dist1=.4
a=np.pi
theCenter=sphere(color=color.red,radius=lengthM/15)
theClock=sphere(size=vector(2.5*lengthM+dist1,2.5*lengthM+dist1,.01),color=vec(.3,.3,.3))
theMarkHand=arrow(pos=vector(0,0,.005),opacity=0,length=lengthM+(dist1)/2)
theHourHand=arrow(pos=vector(0,0,.005),color=color.red,length=2*lengthM/3,axis=vector(0,1,0))
theMinuteHand=arrow(pos=vector(0,0,.005),color=vec(.5,.5,.5),length=lengthM,axis=vector(0,1,0),shaftwidth=lengthM/30)
theSecondHand=arrow(pos=vector(0,0,.005),color=color.white,length=lengthM,axis=vector(0,1,0),shaftwidth=lengthM/60)
theLabel=text(text='Turkey Time',color=vec(.5,.5,1),align='center',pos=vector(0,1.4*lengthM,0))
for i in np.linspace(0,360,361):
    k=(i/180)*a
    theMarkHand.axis=vector(sin(k),cos(k),0)
    if i%30==0:
        if i!=0:
            text(text=str(int(i/30)),color=color.black,pos=vector(sin(k)*(lengthM-dist1),cos(k)*(lengthM-dist1)-lengthM/20,.005),height=lengthM/10,align='center')
        box(axis=vector(sin(k)*(lengthM+(dist1)/2),cos(k)*(lengthM+(dist1)/2),0),pos=vector(sin(k)*(lengthM+(dist1)/2),cos(k)*(lengthM+(dist1)/2),.005),size=vector(.5,.05,.01),color=color.white)
    elif i%6==0:
        box(axis=vector(sin(k)*(lengthM+(dist1)/2),cos(k)*(lengthM+(dist1)/2),0),pos=vector(sin(k)*(lengthM+(dist1)/2),cos(k)*(lengthM+(dist1)/2),.005),size=vector(.2,.01,.01),color=color.white)
    sleep(.000000001)

secondOpacity=1
b=1
i=0
Lred=0
Lgreen=.5
Lblue=.5

wtext(text='Please choose your preferences.Please correct the time after changing the second hand.')

scene.append_to_caption('\n\n')

button(bind=correctionTime,text='Time Configuration',color=color.green,background=vec(.5,.5,.5))

scene.append_to_caption(' Second Hand Type:')

menu(bind=secondOption,choices=['Classic','Smooth','Closed'])

scene.append_to_caption('     ')

radio(bind=changeBackground,text='Clock Color     ')

checkbox(bind=changeHandColor,text='Hand Color')

scene.append_to_caption('\n\n')

slider(bind=redLabel,vertical=False,min=0,max=1,value=0,text='Red')

scene.append_to_caption('     Label Red Percentage')

scene.append_to_caption('\n\n')

slider(bind=greenLabel,vertical=False,min=0,max=1,value=.5,text='Green')

scene.append_to_caption('     Label Green Percentage')

scene.append_to_caption('\n\n')

slider(bind=blueLabel,vertical=False,min=0,max=1,value=.5,text='Blue')

scene.append_to_caption('     Label Blue Percentage')


theTime=time.localtime(time.time())
theHour=theTime.tm_hour
theMinute=theTime.tm_min
theSecond=theTime.tm_sec
i=b*(theHour*3600+theMinute*60+theSecond)
while True:
    i=i+1
    m=(i/180)*a*6
    sleep(1/b)
    theMinuteHand.axis=vector(lengthM*sin(m/(60*b)),lengthM*cos(m/(60*b)),0)
    theHourHand.axis=vector((2*lengthM/3)*sin(m/(720*b)),(2*lengthM/3)*cos(m/(720*b)),0)
    theHourHand.shaftwidth=u
    theSecondHand.axis=vector(lengthM*sin(m/b),lengthM*cos(m/b),0)
    theLabel.color=vec(Lred,Lgreen,Lblue)
    theSecondHand.opacity=secondOpacity
