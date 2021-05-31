import sys
from pynput import keyboard
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

# system tray icon
# app = QApplication(sys.argv)

# trayIcon = QSystemTrayIcon(QIcon('icon.png'), parent=app)
# trayIcon.setToolTip('Typing Speed Tracker')
# trayIcon.show()

# keylogging
count = 0

def on_press(key):
    print('{0}'.format(key))
    k = str(key).replace("'", "")
    
    if key == keyboard.Key.space or key == keyboard.Key.enter:
        write_file("\n")
    elif key == keyboard.Key.insert or key == keyboard.Key.tab or key == keyboard.Key.backspace or key == keyboard.Key.alt or key == keyboard.Key.delete or key == keyboard.Key.end or key == keyboard.Key.home or key == keyboard.Key.esc or key == keyboard.Key.caps_lock or key == keyboard.Key.shift_r or key == keyboard.Key.shift_l or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr or key == keyboard.Key.cmd or key == keyboard.Key.page_down or key == keyboard.Key.page_up or key == keyboard.Key.left or key == keyboard.Key.right or key == keyboard.Key.down or key == keyboard.Key.up:
        pass
    else:
        write_file(k)
    
    # global count
    # try:
    #     print('{0}'.format(key.char), end = '')
        
    # except AttributeError:
    #     # print('{0}'.format(key))
    #     if key == keyboard.Key.space:
    #         print('{0}'.format(' '), end = '')
    #         count += 1
    #         print(count)

def write_file(key):
    with open("log.txt", "a") as f:
        f.write(str(key))


def on_release(key):
    if key == keyboard.Key.insert:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# sys.exit(app.exec_())