import time
import RPi.GPIO as GPIO

class MorseCode():
    """
    MorseCode class for transmitting and receiving messages using Morse code
    """
    def __init__(self, pin, dit_length=0.1):
        """
        Initializes the MorseCode object.

        :param pin: The GPIO pin number to use for transmitting and receiving signals.
        :param dit_length: The length of a "dit" signal, in seconds.
        """
        self.pin = pin
        self.dit_length = dit_length
        self.letters = {
            'a': '.-',    'b': '-...',  'c': '-.-.', 'd': '-..',   'e': '.',
            'f': '..-.',  'g': '--.',   'h': '....', 'i': '..',    'j': '.---',
            'k': '-.-',   'l': '.-..',  'm': '--',   'n': '-.',    'o': '---',
            'p': '.--.',  'q': '--.-',  'r': '.-.',  's': '...',   't': '-',
            'u': '..-',   'v': '...-',  'w': '.--',  'x': '-..-',  'y': '-.--',
            'z': '--..',  '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.'
        }
        self.reverse_letters = {value: key for key, value in self.letters.items()}
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def _transmit_signal(self, length):
        """
        Sends a signal of a certain length.

        :param length: The length of the signal, in seconds.
        """
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(length)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(self.dit_length)

    def _transmit_character(self, character):
        """
        Transmits a single character in Morse code.

        :param character: The character to transmit.
        """
        if character == ' ':
            time.sleep(self.dit_length * 3)
        else:
            for symbol in self.letters[character.lower()]:
                if symbol == '.':
                    self._transmit_signal(self.dit_length)
                else:
                    self._transmit_signal(self.dit_length * 3)

    def transmit_message(self, message):
        """
        Transmits a message in Morse code.

        :param message: The message to transmit.
        """
        for word in message.split(' '):
            for character in word:
                self._transmit_character(character)
            time.sleep(self.dit_length * 3)

    def _receive_signal(self):
        """
        Receives a single signal.

        :return: The length of the signal, in seconds.
        """
        start_time = time.time()
        while GPIO.input(self.pin) == GPIO.HIGH:
            pass
        return time.time() - start_time

    def _receive_character(self):
        """
        Receives a single character in Morse code.

        :return: The character
        """
    def receive_message(self):
        """
        Receives a message in Morse code.

        :return: The received message.
         """
    message = ''
    while True:
        character = ''
        while True:
            signal_length = self._receive_signal()
            if signal_length > self.dit_length * 2:
                if character:
                    message += self.reverse_letters.get(character, '')
                break
            if signal_length > self.dit_length:
                character += '-'
            else:
                character += '.'
        if character == '':
            message += ' '
        if message[-1] == ' ' and len(message) > 1 and message[-2] == ' ':
            break
    return message.strip()

def __del__(self):
    GPIO.cleanup()


"""
Das MorseCode-Modul enthält die Klasse `MorseCode`, die verwendet werden kann, 
um Nachrichten in Morsecode zu übertragen und zu empfangen. 
Die Klasse verwendet das RPi.GPIO-Modul, um Signale auf einem bestimmten GPIO-Pin zu senden und zu empfangen.

Die Klasse `MorseCode` verfügt über die folgenden Methoden:

- `__init__(self, pin, dit_length=0.1)`: Initialisiert das MorseCode-Objekt. `pin` ist die GPIO-Pinnummer, 
die zum Senden und Empfangen von Signalen verwendet wird. `dit_length` ist die Länge eines "dit"-Signals in Sekunden.
- `transmit_message(self, message)`: Sendet eine Nachricht in Morsecode.
- `receive_message(self)`: Empfängt eine Nachricht in Morsecode.
- `__del__(self)`: Wird aufgerufen, wenn das Objekt zerstört wird, und ruft die `GPIO.cleanup()`-Methode auf, um den GPIO-Pin freizugeben.

Das Modul kann wie folgt verwendet werden:

```python
from MorseCode import MorseCode

# Verbindung auf dem GPIO-Pin 18
morse = MorseCode(18)

# Senden einer Nachricht
morse.transmit_message('Hallo Welt')

# Empfangen einer Nachricht
message = morse.receive_message()
print(message)
"""