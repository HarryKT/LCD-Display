## LINE BREAKS

'''
Text will automatically wrap to the next line if the length of the text is greater than the column length of your LCD.
You can also control where the text string breaks to the next line by inserting ````\n\r```` where you want the break to occur.
The code below will print “Hello” to the top row, and “world!” to the bottom row.
'''

from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.write_string("Hello\n\rworld!")

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
