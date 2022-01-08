import keyboard
from datetime import datetime as dt
from time import sleep

MORSE_KEY = ' '
STOP_KEY = 's'

THRESHOLD_MS = 250
PAUSE_THRESHOLD = 2500

morse_alphabet = {
    '*-': 'A',
    '-***': 'B',
    '-*-*': 'C',
    '-**': 'D',
    '*': 'E',
    '**-*': 'F',
    '--*': 'G',
    '****': 'H',
    '**': 'I',
    '*---': 'J',
    '-*-': 'K',
    '*-**': 'L',
    '--': 'M',
    '-*': 'N',
    '---': 'O',
    '*--*': 'P',
    '--*-': 'Q',
    '*-*': 'R',
    '***': 'S',
    '-': 'T',
    '**-': 'U',
    '***-': 'V',
    '*--': 'W',
    '-**': 'X',
    '-*--': 'Y',
    '--*': 'Z'
}

# record keypresses
recording = []
old = dt.now()
while not keyboard.is_pressed(STOP_KEY):
    if keyboard.is_pressed(MORSE_KEY):
        recording.append(((dt.now()-old).microseconds//1000,0))
        old = dt.now()
        while keyboard.is_pressed(MORSE_KEY):
            pass
        recording.append(((dt.now()-old).microseconds//1000,1))
        old = dt.now()

# interpret presses and pauses
for entry in recording:
    millis, state = entry
    if (state = 0):
        pass