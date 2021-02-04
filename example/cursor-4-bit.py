## TURN THE CURSOR ON AND OFF

'''
The RPLCD library provides several functions for controlling the cursor.
You can have a block cursor, an underline cursor, or a blinking cursor. Use the following functions to set the cursor:

Blinking block cursor: 'lcd.cursor_mode = "blink"'
Line cursor: 'lcd.cursor_mode = "line"'
Cursor off: 'lcd.cursor_mode = "hide"'
The code below places a blinking cursor after the last character of text:
'''

from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.write_string("Hello world!")

lcd.cursor_mode = "blink"
# lcd.cursor_mode = "line"
# lcd.cursor_mode = "hide"

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
