## PRINTING A SINGLE CUSTOM CHARACTER

'''
Take a look at this code, which prints a single smiley face character to the display:
'''

from RPLCD import CharLCD, cleared, cursor  # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

smiley = (
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b10001,
    0b01110,
    0b00000,
)
lcd.create_char(0, smiley)
lcd.write_string(unichr(0))

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
