## PRINT YOUR IP ADDRESS

'''
This program will print the IP address of your ethernet connection to the LCD.
To print the IP of your WiFi connection, just change eth0 in line 19 to wlan0:
'''

from RPLCD import CharLCD                   # This is the library which we will be using for LCD Display 
from RPi import GPIO                        # This is the library which we will be using for using the GPIO pins of Raspberry PI
import socket                               # This is the library which we will be using to check the socket and find IP
import fcntl
import struct

# Initializing the LCD Display
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd.write_string("IP Address:") 

lcd.cursor_pos = (1, 0)
lcd.write_string(get_ip_address('eth0'))

# Always Clean Up the GPIO after using the code
GPIO.cleanup()
