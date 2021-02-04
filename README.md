# LCD-Display
Integration of 16x2 LCD display with Raspberry PI


## CONNECTING THE LCD
There are two ways to connect the LCD to your Raspberry Pi – in 4 bit mode or 8 bit mode. 4 bit mode uses 6 GPIO pins, while 8 bit mode uses 10. Since it uses up less pins, 4 bit mode is the most common method, but I’ll explain how to set up and program the LCD both ways.

Each character and command is sent to the LCD as a byte (8 bits) of data. In 8 bit mode, the byte is sent all at once through 8 data wires, one bit per wire. In 4 bit mode, the byte is split into two sets of 4 bits – the upper bits and lower bits, which are sent one after the other over 4 data wires.

Theoretically, 8 bit mode transfers data about twice as fast as 4 bit mode, since the entire byte is sent all at once. However, the LCD driver takes a relatively long time to process the data, so no matter which mode is being used, we don’t really notice a difference in data transfer speed between 8 bit and 4 bit modes.


## WIRING THE LCD IN 8 BIT MODE
To connect your LCD in 8 bit mode set it up like this:

<img src="https://github.com/HarryKT/LCD-Display/blob/main/images/Raspberry-Pi-LCD-8-Bit-Mode-Connection-Diagram-768x1024.png" alt="Wiring for 8 Bit Mode" />

The backlight and contrast potentiometers are 10K Ohms, but they can be substituted with 1K to 3K Ohm resistors if you want.


## WIRING THE LCD IN 4 BIT MODE
To connect the LCD to your Raspberry Pi in 4 bit mode, set it up like this:

<img src="https://github.com/HarryKT/LCD-Display/blob/main/images/Raspberry-Pi-LCD-4-bit-mode-719x1024.png" alt="Wiring for 4 Bit Mode" />

The potentiometers here can also be substituted with 1K or 3K Ohm resistors.

## PROGRAMMING THE LCD WITH PYTHON
If this is your first time writing and running a Python program, you might want to read <a href="https://www.circuitbasics.com/?p=214283" target="_blank">How to Write and Run a Python Program on the Raspberry Pi</a>, which will explain everything you need to know to run the examples below.

We’ll be using a Python library that provides a lot of useful functions. Its called the RLPCD library, and was written by Danilo Bargen.


## INSTALLING THE RPLCD LIBRARY

For all platforms (Raspberry Pi and Beaglebone Black) make sure you have the following dependencies:
````
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip
````

For a Raspberry Pi make sure you have the RPi.GPIO library by executing:
````
sudo pip install RPi.GPIO
````

The RPLCD library can be installed from the Python Package Index, or PIP. It might already be installed on your Pi, but if not, enter this at the command prompt to install it:
````
sudo apt-get install python-pip
````

After you get PIP installed, install the RPLCD library by entering:
````
sudo pip install RPLCD
````

The example programs in the Example folder use the Raspberry Pi’s physical pin numbers, not the BCM or GPIO numbers. I’m assuming you have your LCD connected the way it is in the diagrams above, but I’ll show you how to change the pin connections if you need to.

## Most Important
Except write-8-bit.py all the examples are written for 4 Bit Mode.
