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

def on_press(key):
    global keystoke_count
        
    if key == keyboard.Key.f12 or key == keyboard.Key.f11 or key == keyboard.Key.f10 or key == keyboard.Key.f9 or key == keyboard.Key.f8 or key == keyboard.Key.f7 or key == keyboard.Key.f6 or key == keyboard.Key.f5 or key == keyboard.Key.f4 or key == keyboard.Key.f3 or key == keyboard.Key.f2 or key == keyboard.Key.f1 or key == keyboard.Key.print_screen or key == keyboard.Key.media_play_pause or key == keyboard.Key.media_volume_up or key == keyboard.Key.media_volume_down or key == keyboard.Key.media_volume_mute or key == keyboard.Key.space or key == keyboard.Key.enter or key == keyboard.Key.insert or key == keyboard.Key.tab or key == keyboard.Key.alt or key == keyboard.Key.delete or key == keyboard.Key.end or key == keyboard.Key.home or key == keyboard.Key.esc or key == keyboard.Key.caps_lock or key == keyboard.Key.shift_r or key == keyboard.Key.shift_l or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r or key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr or key == keyboard.Key.cmd or key == keyboard.Key.page_down or key == keyboard.Key.page_up or key == keyboard.Key.left or key == keyboard.Key.right or key == keyboard.Key.down or key == keyboard.Key.up:
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