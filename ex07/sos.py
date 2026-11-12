import sys


def morse_decode(txt: str) -> str:
    """ convert txt to morse code """
    NESTED_MORSE = {
        'A': '.-',      'B': '-...',    'C': '-.-.',
        'D': '-..',     'E': '.',       'F': '..-.',
        'G': '--.',     'H': '....',    'I': '..',
        'J': '.---',    'K': '-.-',     'L': '.-..',
        'M': '--',      'N': '-.',      'O': '---',
        'P': '.--.',    'Q': '--.-',    'R': '.-.',
        'S': '...',     'T': '-',       'U': '..-',
        'V': '...-',    'W': '.--',     'X': '-..-',
        'Y': '-.--',    'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
    }
    try:
        morse = [NESTED_MORSE[c.upper()] for c in txt]
        msg = " ".join(morse)
    except KeyError:
        raise AssertionError(
            "AssertionError: the arguments are bad")
    return msg


def main():
    """ print morse code from arg """
    arg = sys.argv[1:]
    try:
        if len(arg) != 1:
            raise AssertionError(
                "AssertionError: the arguments are bad")
        print(morse_decode(arg[0]))
    except AssertionError as a:
        return print(a)


if __name__ == "__main__":
    main()
