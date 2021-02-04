## PRINTING MULTIPLE CUSTOM CHARACTERS

'''
This program will print the Greek letters omega, pi, and mu, along with symbols for temperature (a thermometer) and humidity (a water drop):
'''

from RPLCD import CharLCD, cleared, cursor  # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

omega = (
    0b00000,
    0b01110,
    0b10001,
    0b10001,
    0b10001,
    0b01010,
    0b11011,
    0b00000,
)

pi = (
    0b00000,
    0b00000,
    0b11111,
    0b01010,
    0b01010,
    0b01010,
    0b10011,
    0b00000,
)

mu = (
    0b00000,
    0b10010,
    0b10010,
    0b10010,
    0b10010,
    0b11101,
    0b10000,
    0b10000,
)

drop = (
    0b00100,
    0b00100,
    0b01010,
    0b01010,
    0b10001,
    0b10001,
    0b10001,
    0b01110,
)

temp = (
    0b00100,
    0b01010,
    0b01010,
    0b01110,
    0b01110,
    0b11111,
    0b11111,
    0b01110,
)

lcd.create_char(0, omega)
lcd.create_char(1, pi)
lcd.create_char(2, mu)
lcd.create_char(3, drop)
lcd.create_char(4, temp)

lcd.write_string(unichr(0))
lcd.write_string(unichr(1))
lcd.write_string(unichr(2))
lcd.write_string(unichr(3))
lcd.write_string(unichr(4))

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
