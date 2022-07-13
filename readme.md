# TypeMeter
This is a simple typing speed tracking application which calculates the wpm in live time as the user keeps typing. 

#### NOTE:
This program requires the pynput module to execute.

To install pynput, you can install it with pip.
```
pip install pynput
```

## TUI
This program offers a Terminal User Interface when running the app as of now. 

You run the program in the terminal of your choice with the following command.

```
python InstantTracker.py
```
And the program would run in the terminal displaying such output.
![Program Output](https://github.com/Igneel001/TypeMeter/blob/main/screenshots/program_ss.PNG)

After running the program, you can minimize the terminal and start typing normally anywhere on your computer. It'll keep reading and calculating the typing speed every second. 

When done, hit insert and the program will terminate, giving you the average wpm and average cpm since the program started execution. 

## Future Enhancements
- Improved algorithm
- GUI
- Run as a background process