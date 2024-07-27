import pynput
import time
#import pyautogui
#import pywinauto
'''import pyperclip
pyperclip.copy('Hey!')
print(pyperclip.paste())'''

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        
def on_release(key):
    print('{0} released'.format(
        key))
    
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    if pressed:
        print('Pressed '+str(button)+' at '+str(x)+','+str(y))
    else:
        print('Released '+str(button)+' at '+str(x)+','+str(y))

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    
mouseController=pynput.mouse.Controller()
mouseListener=pynput.mouse.Listener(on_click=on_click,on_move=on_move,on_scroll=on_scroll)

keyboardController=pynput.keyboard.Controller()
keyboardListener=pynput.keyboard.Listener(on_press=on_press, on_release=on_release)

keyboardListener.start()
mouseListener.start()
while 'xd':
    #mouseController.move(1365,767)

    print(mouseController.position)

    #mouseController.click(pynput.mouse.Button.right)

    #keyboardController.type('Hello!')

    #keyboardController.press(pynput.keyboard.Key.alt_l)
    #keyboardController.press(pynput.keyboard.Key.tab)
    #keyboardController.release(pynput.keyboard.Key.tab)
    #keyboardController.release(pynput.keyboard.Key.alt_l)
    #time.sleep(.1)
    #keyboardController.press(pynput.keyboard.Key.enter)

    time.sleep(2)