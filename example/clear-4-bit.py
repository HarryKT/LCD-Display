## CLEAR THE SCREEN

'''
The function lcd.clear() will clear the screen.
The following code will print “Hello world!” to the screen for two seconds before clearing it:
'''

import time                                 # This is the library which we will be using for the time function
from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.write_string("Hello world!")

time.sleep(2)                               # This will hold the code here for 2 seconds
lcd.clear()                                 # And this clears the LCD Display

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
