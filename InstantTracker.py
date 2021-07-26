import sys
import time
import threading
from pynput import keyboard
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 


keystrokeCount = 0
wordCount = 1
tempCount = 0
avgWpm = 0
"""
Removed: 
clearCount,Keystrokes in main
parameter words in func wpm
snippet to clear keystrokes
"""

"""
Added:
AND COMMENTED lpm var in func wpm (It seems a little odd to display)
wordStartTime in main
TimePeriod in func on_release
changed avg letter count to become a word as 5 instead of 4(The if condition)

"""

"""
ignoredKeystrokes:

ERROR

 keyboard.Key.prinont_screen, keyboard.Key.media_play_pause,
"""

ignoredKeystrokes = [
                        keyboard.Key.f12, keyboard.Key.f11, keyboard.Key.f10, keyboard.Key.f9, keyboard.Key.f8, 
                        keyboard.Key.f7, keyboard.Key.f6, keyboard.Key.f5, keyboard.Key.f4, keyboard.Key.f3,                         
                        keyboard.Key.media_volume_up, keyboard.Key.media_volume_down, keyboard.Key.media_volume_mute, 
                        keyboard.Key.space, keyboard.Key.enter, keyboard.Key.insert, keyboard.Key.tab, keyboard.Key.alt,
                        keyboard.Key.delete, keyboard.Key.end, keyboard.Key.home, keyboard.Key.esc, keyboard.Key.caps_lock,
                        keyboard.Key.shift_r, keyboard.Key.shift_l, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt_l,
                        keyboard.Key.alt_gr, keyboard.Key.cmd, keyboard.Key.page_down, keyboard.Key.page_up, keyboard.Key.left, 
                        keyboard.Key.right, keyboard.Key.down, keyboard.Key.up,keyboard.Key.f2, keyboard.Key.f1,
                    ]

startTime = wordStartTime = endTime = -1.0

def on_press(key):
    global keystrokeCount, wordCount, tempCount,  wordStartTime,startTime,endTime

    if startTime==-1:
        startTime = wordStartTime = time.time()
    
    executionTime=0
    if key in ignoredKeystrokes:
        pass
    
    elif key == keyboard.Key.backspace:
        if keystrokeCount == 0:
            pass
        else:
            keystrokeCount -= 1
            tempCount -= 1
            if tempCount == 0:
                wordCount -= 1
                tempCount = 4
    
    else:
        keystrokeCount += 1
        
        endTime=time.time()

        if tempCount == 4:
            wordCount += 1
            tempCount = 1
            executionTime = (time.time() - wordStartTime)
            wordStartTime=time.time()
        else:
            tempCount += 1
        

    if executionTime!=0:
        t = threading.Timer(executionTime, wpm, [executionTime])
        t.start()

def wpm(TimePeriod):
    global wordCount,avgWpm
    wpm = 60 / TimePeriod
    if avgWpm==0:
        avgWpm=wpm 
    else:
        avgWpm = (avgWpm+wpm)/2
    #lpm = 60*4*(1/TimePeriod)
    print("WPM: ", round(wpm))
    print("Avg WPM: ",round(avgWpm))

def on_release(key):
    TimePeriod = endTime-startTime
    if key == keyboard.Key.insert:
        print("Word count:      ", wordCount)
        print("Keystroke count: ", keystrokeCount)
        print("Avg words per min: ",round(wordCount*(60/TimePeriod)))
        print("Avg letters per min:", round(keystrokeCount*(60/TimePeriod)))
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
