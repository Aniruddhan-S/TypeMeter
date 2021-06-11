import sys
import time
import threading
from pynput import keyboard
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

# system tray icon
# app = QApplication(sys.argv)

# trayIcon = QSystemTrayIcon(QIcon('icon.png'), parent=app)
# trayIcon.setToolTip('Typing Speed Tracker')
# trayIcon.show()

keystrokes = []
keystrokeCount = 0
wordCount = 1
tempCount = 0
clearCount = 0

ignoredKeystrokes = [
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

startTime = time.time()

def on_press(key):
    global keystrokeCount, wordCount, tempCount, clearCount, startTime
    
    if key in ignoredKeystrokes:
        pass
    
    elif key == keyboard.Key.backspace:
        if len(keystrokes) == 0:
            pass
        else:
            keystrokes.pop()
            keystrokeCount -= 1
            tempCount -= 1
            if tempCount == 0:
                wordCount -= 1
                tempCount = 4
    
    else:
        keystrokeCount += 1
        clearCount += 1
        keystrokes.append(key)
        
        if tempCount == 4:
            wordCount += 1
            tempCount = 1
        else:
            tempCount += 1
        
    if clearCount == 100:
        keystrokes.clear()
        clearCount = 0

    executionTime = (time.time() - startTime)
    
    t = threading.Timer(3.0, wpm, [wordCount, round(executionTime)])
    t.start()

def wpm(words, currentTime):
    wpm = words * (60 / currentTime)
    print("WPM: ", round(wpm))

def on_release(key):
    if key == keyboard.Key.insert:
        print("Word count:      ", wordCount)
        print("Keystroke count: ", keystrokeCount)     
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# sys.exit(app.exec_())