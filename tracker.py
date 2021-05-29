import pynput
from pynput import keyboard

count = 0

def on_press(key):
    global count
    try:
        print('alphanumeric key:     {0}'.format(key.char))
        
    except AttributeError:
        print('special key:          {0}'.format(key))
        if key == keyboard.Key.space:
            count += 1
            print(count)


def on_release(key):
    if key == keyboard.Key.insert:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()