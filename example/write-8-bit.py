## WRITE TO THE DISPLAY IN 8 BIT MODE

'''
Let’s start with a simple program that will display “Hello world!” on the LCD. 
If you have a different sized LCD than the 16×2 I’m using (like a 20×4), change the number of columns and rows in line 2 of the code. 
cols= sets the number of columns, and rows= sets the number of rows. 
You can also change the pins used for the LCD’s RS, E, and data pins. 
The data pins are set as pins_data=[D0, D1, D2, D3, D4, D5, D6, D7].
Text strings are written to the display using the lcd.write_string() function:
'''

from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])
lcd.write_string(u'Hello world!')

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
