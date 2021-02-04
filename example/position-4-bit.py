## POSITION THE TEXT

'''
The text can be positioned anywhere on the screen using lcd.cursor_pos = (ROW, COLUMN).
The rows are numbered starting from zero, so the top row is row 0, and the bottom row is row 1. 
Similarly, the columns are numbered starting at zero, so for a 16×2 LCD the columns are numbered 0 to 15. 
For example, the code below places “Hello world!” starting at the bottom row, fourth column:
'''

from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

lcd.cursor_pos = (1, 3)                     # This will place the cursor at row=(1+1)=2 and col=(3+1)=4
lcd.write_string("Hello world!")

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
