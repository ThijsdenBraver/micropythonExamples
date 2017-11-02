# Copyright by Thijs den Braver 2017

# PIN LAYOUT VOOR DE WEMOS:
# led 1 = pin 12
# led 2 = pin 13
# led 3 = pin 14
# led 4 = pin 15
# led 5 = pin 16
# scherm = pin 5 & 4

# Import alle dependencies.
import machine
from machine import Pin, PWM, I2C
import time
import ssd1306  
import sys

# Maak een array waar de waardes in kunnen worden doorgegeven.
ledlist = [0, 0, 0, 0, 0]

# Defineer alle hardware
i2c = I2C(-1, Pin(5), Pin(4))
led1 = machine.Pin(12, machine.Pin.OUT)
led2 = machine.Pin(13, machine.Pin.OUT)
led3 = machine.Pin(14, machine.Pin.OUT)
led4 = machine.Pin(15, machine.Pin.OUT)
led5 = machine.Pin(16, machine.Pin.OUT)
display = ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)

# Laat ff de creator op het scherm zien.
display.text('Knight Rider', 1, 0)
display.text('Made By:', 1, 15)
display.text("Thijs den Braver", 1, 25)
display.show()

# De loop wat het programma telkens moet doen.
while True:

	# Defineert een functie die array's afgaat in een array en de leds aan/uit zet naar aanleiding van de array's in de array.
	def setLed(invoer):
		for frame in range(0, len(invoer)):
			if invoer[frame][0] == 1:
				led1.on()
			else:
				led1.off()

			if invoer[frame][1] == 1:
				led2.on()
			else:
				led2.off()

			if invoer[frame][2] == 1:
				led3.on()
			else:
				led3.off()

			if invoer[frame][3] == 1:
				led4.on()
			else:
				led4.off()

			if invoer[frame][4] == 1:
				led5.on()
			else:
				led5.off()

			time.sleep(.2)

	# Voerd de functie hierboven uit met een nightrider patroon.
	setLed([[1, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 1, 0],[0, 0, 0, 0, 1],[0, 0, 0, 1, 0],[0, 0, 0, 1, 0],[0, 0, 1, 0, 0],[0, 1, 0, 0, 0]])



