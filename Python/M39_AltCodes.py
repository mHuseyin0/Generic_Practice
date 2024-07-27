import pynput.keyboard as kb
alt = kb.Key.alt_l
keyboardController = kb.Controller()
press = keyboardController.press
release = keyboardController.release
tap = keyboardController.tap
numPadKeys = []
for key in range(96,106):
    numPadKeys.append(kb.KeyCode.from_vk(key))

def intToKeyOrder(number:int):
    number = str(number)
    orderList = []
    for figure in number:
        match(figure):
            case "0": orderList.append(numPadKeys[0])
            case "1": orderList.append(numPadKeys[1])
            case "2": orderList.append(numPadKeys[2])
            case "3": orderList.append(numPadKeys[3])
            case "4": orderList.append(numPadKeys[4])
            case "5": orderList.append(numPadKeys[5])
            case "6": orderList.append(numPadKeys[6])
            case "7": orderList.append(numPadKeys[7])
            case "8": orderList.append(numPadKeys[8])
            case "9": orderList.append(numPadKeys[9])
    return orderList
from time import sleep

for i in range(1,261):
    keyboardController.type(str(i))
    tap(kb.Key.right)
    tap(kb.Key.space)
    press(alt)
    for key in intToKeyOrder(i):
        tap(key)
    release(alt)
    tap(kb.Key.enter)
    tap(kb.Key.left)
    if i % 26 == 0:
        tap(kb.Key.right)
        tap(kb.Key.right)
        press(kb.Key.ctrl_l)
        tap(kb.Key.up)
        release(kb.Key.ctrl_l)