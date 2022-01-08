import keyboard
from datetime import datetime as dt, timedelta
import interpreter

MORSE_KEY = ' '
STOP_KEY = 's'

THRESHOLD_MS = 140
CHAR_PAUSE_THRESHOLD = 350
WORD_PAUSE_THRESHOLD = 1400

total = lambda delta: delta / timedelta(milliseconds=1)

# record keypresses
recording = []
try:
    while True:
        old = dt.now()
        while not keyboard.is_pressed(MORSE_KEY):
            pass
        recording.append((total(dt.now()-old),0))
        old = dt.now()
        while keyboard.is_pressed(MORSE_KEY):
            pass
        recording.append((total(dt.now()-old),1))
except KeyboardInterrupt:
    pass

message = interpreter.interpret_morse(recording, THRESHOLD_MS, CHAR_PAUSE_THRESHOLD, WORD_PAUSE_THRESHOLD)
print(repr(message))