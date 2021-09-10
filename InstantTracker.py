# IMPORTS
import os
import datetime
import time
import threading
from pynput import keyboard
from stat import S_IREAD, S_IWRITE


# ASCII ART
print(" _____                 __  __      _")
print("|_   _|   _ _ __   ___|  \/  | ___| |_ ___ _ __")
print("  | || | | | '_ \ / _ \ |\/| |/ _ \ __/ _ \ '__|")
print("  | || |_| | |_) |  __/ |  | |  __/ ||  __/ |")
print("  |_| \__, | .__/ \___|_|  |_|\___|\__\___|_|")
print("      |___/|_|")
print("\n Press insert to exit the program\n")


# GLOBAL VARIABLES
keystrokeCount = 0
wordCount = 1
tempCount = 0
liveAvgWpm = 0
pr = 0
avgWPM = 0
avgCPM = 0


# KEYSTROKES TO BE IGNORED
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


# MAIN ALGORITHM
def on_press(key):
    global keystrokeCount, wordCount, tempCount, wordStartTime, startTime, endTime

    if startTime ==- 1:
        startTime = wordStartTime = time.time()
    
    executionTime = 0
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
            wordStartTime = time.time()
        else:
            tempCount += 1
        

    if executionTime != 0:
        t = threading.Timer(executionTime, wpm, [executionTime])
        t.start()


# DISPLAY WPM
def wpm(TimePeriod):
    global liveAvgWpm

    liveWpm = 60 / TimePeriod
    if liveAvgWpm == 0:
        liveAvgWpm = liveWpm 
    else:
        liveAvgWpm = (liveAvgWpm+liveWpm)/2
    print("WPM: ", round(liveAvgWpm))
    

# END PROGRAM
def on_release(key):
    global avgWPM, avgCPM
    TimePeriod = endTime - startTime
   
    if key == keyboard.Key.insert:
        avgWPM = round(wordCount*(60/TimePeriod))
        avgCPM = round(keystrokeCount*(60/TimePeriod))
 
        print("Session duration: ", round(TimePeriod), "seconds")
        print("Avg WPM: ", avgWPM)
        print("Avg CPM: ", avgCPM)
        sessions(TimePeriod)
        PR()
        return False


# SAVE SESSION INFO
def sessions(timeperiod):
    date = datetime.datetime.now()
   
    try: 
        f = open("sessions.txt", 'a')
    except PermissionError:
        os.chmod("sessions.txt", S_IWRITE)
        f = open("sessions.txt", 'a')
    
    f.write("\nDATE: %s/%s/%s" % (date.day, date.month, date.year))
    f.write("\nTIME: %s" % (time.strftime("%I:%M:%S %p")))
    f.write("\n\nSession duration: %s seconds" % (round(timeperiod)))
    f.write("\nAvg WPM: %s" % avgWPM)
    f.write("\nAvg CPM: %s" % avgCPM)
    f.write("\n\n--------------------------------------------\n")
    f.close()

    os.chmod("sessions.txt", S_IREAD)


def PR():
    global pr
    if pr < avgWPM: 
        pr = avgWPM
        print(" _________________________________________ ")
        print("/ Congralutations! You beat your Personal \ ")
        print("\ Record!                                 / ")
        print(" ----------------------------------------- ")
        print("        \   ^__^ ")
        print("         \  (oo)\_______ ")
        print("            (__)\       )\/\ ")
        print("                ||-----|| ")
        print("                ||     || ")
    else:
        print("\n Your Personal Record:", pr)


# EVENT LISTENER
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
