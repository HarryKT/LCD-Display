## WRITE TO THE DISPLAY IN 4 BIT MODE

'''
In 4 bit mode, only LCD pins D4, D5, D6, and D7 are used for data.
These are set in pins_data=[D4, D5, D6, D7] on line 2 below:
'''

from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.write_string("Hello world!")

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
