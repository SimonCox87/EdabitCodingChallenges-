"""Create a function that takes a string as an argument and returns the Morse code equivalent.
Examples

encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--

Notes

    Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
    Input value can be lower or upper case.
    Input string can have digits.
    Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
    One space " " is expected after each character, except the last one."""

def encode_morse(message):
    message = message.upper()

    char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    
    morseString = []

    for l in message:
        for char in char_to_dots.keys():
            if l == char:
                morseString.append(char_to_dots[char])
    
    return " ".join(morseString)

print(encode_morse("EDABBIT CHALLENGE"))
print(encode_morse("HELP ME !"))

"""def encode_morse(txt):
	d = {'A':'.-', 'B':'-...',
		 'C':'-.-.', 'D':'-..', 'E':'.',
		 'F':'..-.', 'G':'--.', 'H':'....',
		 'I':'..', 'J':'.---', 'K':'-.-',
		 'L':'.-..', 'M':'--', 'N':'-.',
		 'O':'---', 'P':'.--.', 'Q':'--.-',
		 'R':'.-.', 'S':'...', 'T':'-',
		 'U':'..-', 'V':'...-', 'W':'.--',
		 'X':'-..-', 'Y':'-.--', 'Z':'--..',
		 '1':'.----', '2':'..---', '3':'...--',
		 '4':'....-', '5':'.....', '6':'-....',
		 '7':'--...', '8':'---..', '9':'----.',
		 '0':'-----', ',':'--..--', '.':'.-.-.-',
		 '?':'..--..', '/':'-..-.', '-':'-....-',
		 '(':'-.--.', ')':'-.--.-', '!': '-.-.--', 
		 ' ': ' ', "'": '.----.', ':': '---...'}
		 
	return ' '.join(d[i] for i in txt.upper())"""