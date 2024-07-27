from time import *
from threading import Thread

def myBox(delayT):
    while True:
        print('The box is open.')
        sleep(delayT)
        print('The box is closed.')
        sleep(delayT)
def myLED(delayT):
    while True:
        print('The LED is on.')
        sleep(delayT)
        print('The LED is off.')
        sleep(delayT)
delayBox=5
delayLED=1
boxThread=Thread(target=myBox, args=(delayBox,))
LEDThread=Thread(target=myLED, args=(delayLED,))
boxThread.start()
LEDThread.start()
