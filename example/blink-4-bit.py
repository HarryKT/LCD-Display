## BLINKING TEXT

'''
Combining lcd.clear() and time.sleep() in a while loop will produce a blinking text effect:
'''

import time                                 # This is the library which we will be using for the time function
from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

while True:
    lcd.write_string(u"Hello world!")
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
    
## Press Ctrl+C to exit the program.
