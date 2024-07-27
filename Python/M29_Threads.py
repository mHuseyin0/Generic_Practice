from concurrent.futures import ThreadPoolExecutor
from threading import Lock, RLock
from time import sleep
import time
import pynput
import math

theLock = Lock()
# acquire() and release() methods can be used, but context managers are recommended due to weird bugs.
secondLock = RLock()
# This can be locked many times.It should be released the times it has been acquired to unlock.
# This exists to prevent deadlocks.(When a lock cannot be released properly due to a bug or a design issue.)

def mouseCircle():
    mouseController = pynput.mouse.Controller()
    mouseController.move(-1500,-1800)
    mouseController.move(579,380)
    x = 579
    y = 380
    for _ in range(101):    
        x+=1
        yNew = int(math.sqrt(math.pow(100,2) - math.pow(x-680,2)) + 380)
        yMove = yNew - mouseController.position[1]
        mouseController.move(1,yMove)
        sleep(.05)
    with theLock:
        print(mouseController.position)

    for _ in range(100):
        x+=1
        yNew = int(math.sqrt(math.pow(100,2) - math.pow(x-680,2)) + 380)
        yMove = yNew - mouseController.position[1]
        mouseController.move(1,yMove)
        sleep(.05)
    with theLock:
        print(mouseController.position)

    for _ in range(100):
        x-=1
        yNew = int(-math.sqrt(math.pow(100,2) - math.pow(x-680,2)) + 380)
        yMove = yNew - mouseController.position[1]
        mouseController.move(-1,yMove)
        sleep(.05)
    with theLock:
        print(mouseController.position)

    for _ in range(100):
        x-=1
        yNew = int(-math.sqrt(math.pow(100,2) - math.pow(x-680,2)) + 380)
        yMove = yNew - mouseController.position[1]
        mouseController.move(-1,yMove)
        sleep(.05)
    with theLock:
        print(mouseController.position)
    return "Number 1 finished."

def timer():
    second = 0
    temp = 0
    times = []
    while second<20:
        times.append(time.perf_counter() - temp)
        temp = time.perf_counter()
        with theLock:
            print("Time:",second)
        second+=1
        sleep(1)
    return times

def counter(name):
    x = 0
    while x<10000000:
        if x%1000000 == 0:
            with theLock:
                print("x:",x)
        x+=1
    with theLock:
        print(name, "has finished!")

with ThreadPoolExecutor(max_workers=5) as myThreads:
    x1 = myThreads.submit(mouseCircle)
    x2 = myThreads.submit(timer)
    myThreads.map(counter,range(4))

print(x1.result(),x2.result())
