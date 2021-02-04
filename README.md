# LCD-Display
Integration of 16x2 LCD display with Raspberry PI

## CONNECTING THE LCD
There are two ways to connect the LCD to your Raspberry Pi – in 4 bit mode or 8 bit mode. 4 bit mode uses 6 GPIO pins, while 8 bit mode uses 10. Since it uses up less pins, 4 bit mode is the most common method, but I’ll explain how to set up and program the LCD both ways.

Each character and command is sent to the LCD as a byte (8 bits) of data. In 8 bit mode, the byte is sent all at once through 8 data wires, one bit per wire. In 4 bit mode, the byte is split into two sets of 4 bits – the upper bits and lower bits, which are sent one after the other over 4 data wires.

Theoretically, 8 bit mode transfers data about twice as fast as 4 bit mode, since the entire byte is sent all at once. However, the LCD driver takes a relatively long time to process the data, so no matter which mode is being used, we don’t really notice a difference in data transfer speed between 8 bit and 4 bit modes.

## WIRING THE LCD IN 8 BIT MODE
To connect your LCD in 8 bit mode set it up like this:

![alt text](https://github.com/HarryKT/LCD-Display/blob/[branch]/image.jpg?raw=true)
