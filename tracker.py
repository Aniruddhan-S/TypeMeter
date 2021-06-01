import sys
from pynput import keyboard
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

# system tray icon
# app = QApplication(sys.argv)

# trayIcon = QSystemTrayIcon(QIcon('icon.png'), parent=app)
# trayIcon.setToolTip('Typing Speed Tracker')
# trayIcon.show()

keystrokes = []
keystoke_count = 0

ignored_keystrokes = [
                        keyboard.Key.f12, keyboard.Key.f11, keyboard.Key.f10, keyboard.Key.f9, keyboard.Key.f8, 
                        keyboard.Key.f7, keyboard.Key.f6, keyboard.Key.f5, keyboard.Key.f4, keyboard.Key.f3, 
                        keyboard.Key.f2, keyboard.Key.f1, keyboard.Key.print_screen, keyboard.Key.media_play_pause,
                        keyboard.Key.media_volume_up, keyboard.Key.media_volume_down, keyboard.Key.media_volume_mute, 
                        keyboard.Key.space, keyboard.Key.enter, keyboard.Key.insert, keyboard.Key.tab, keyboard.Key.alt,
                        keyboard.Key.delete, keyboard.Key.end, keyboard.Key.home, keyboard.Key.esc, keyboard.Key.caps_lock,
                        keyboard.Key.shift_r, keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_l,
                        keyboard.Key.alt_gr, keyboard.Key.cmd, keyboard.Key.page_down, keyboard.Key.page_up, keyboard.Key.left, 
                        keyboard.Key.right, keyboard.Key.down, keyboard.Key.up
                    ]

def on_press(key):
    global keystoke_count
        
    if key in ignored_keystrokes:
        pass
    
    elif key == keyboard.Key.backspace:
        if len(keystrokes) == 0:
            pass
        else:
            keystrokes.pop()
            keystoke_count -= 1
    
    else:
        keystoke_count += 1
        keystrokes.append(key)

    print(keystrokes)
    print( keystoke_count)

def on_release(key):
    if key == keyboard.Key.insert:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# sys.exit(app.exec_())