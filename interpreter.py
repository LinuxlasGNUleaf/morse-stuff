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
    '--**': 'Z'
}

def interpret_morse(recording, THRESHOLD_MS, CHAR_PAUSE_THRESHOLD, WORD_PAUSE_THRESHOLD):
    message = ''
    current_symbol = ''
    for entry in recording:
        millis, state = entry
        if state == 1:
            if millis <= THRESHOLD_MS:
                current_symbol += '*'
            else:
                current_symbol += '-'
        elif state == 0:
            if millis >= CHAR_PAUSE_THRESHOLD: # symbol done, decode current symbol
                if current_symbol:
                    message += decode_symbol(current_symbol)
                    if millis >= WORD_PAUSE_THRESHOLD: # if th
                        message += ' '
                    current_symbol = ''
            else:
                pass
    
    if current_symbol:
        message += decode_symbol(current_symbol)
    return message

def decode_symbol(symbol):
    print(symbol)
    if symbol in morse_alphabet:
        return morse_alphabet[symbol]
    else:
        return '?'

if __name__ == '__main__':
    msg = [( 783, 0),
        (  63, 1), # *
        ( 173, 0),
        ( 100, 1), # *
        ( 208, 0),
        (  62, 1), # *
        ( 783, 0),
        ( 603, 1), # -
        ( 173, 0),
        (1000, 1), # -
        ( 208, 0),
        ( 602, 1), # -
        ( 783, 0),
        ( 163, 1), # *
        ( 173, 0),
        ( 120, 1), # *
        ( 208, 0),
        ( 162, 1)] # *

    print(repr(interpret_morse(msg, 200, 400, 800)))