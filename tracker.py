import sys
from pynput import keyboard
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

# system tray icon
app = QApplication(sys.argv)

trayIcon = QSystemTrayIcon(QIcon('icon.png'), parent=app)
trayIcon.setToolTip('Typing Speed Tracker')
trayIcon.show()

# keylogging
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

sys.exit(app.exec_())