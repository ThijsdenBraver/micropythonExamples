# Copyright by Thijs den Braver 2017

# PIN LAYOUT VOOR DE WEMOS:
# led 1 = pin 12
# led 2 = pin 13
# led 3 = pin 14
# led 4 = pin 15
# scherm = pin 5 & 4
# servo = pin 0
# button up = pin 2
# button down = pin 0


# Import alle dependencies.
import machine
from machine import Pin, PWM, I2C
import time
import ssd1306  
import sys

# Defineer alle hardware en variabelen.
servo = PWM(Pin(0), freq=50, duty=77)   
i2c = I2C(-1, Pin(5), Pin(4))
number = 0
buttondown = machine.Pin(16, machine.Pin.IN)
buttonup = machine.Pin(2, machine.Pin.IN)
led1 = machine.Pin(12, machine.Pin.OUT)
led2 = machine.Pin(13, machine.Pin.OUT)
led3 = machine.Pin(14, machine.Pin.OUT)
led4 = machine.Pin(15, machine.Pin.OUT)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

# Laat ff de creator op het scherm zien.
display.fill(0)
display.text('Press any button:' + ' ' + str(number), 1, 0)
display.text('Made By:', 1, 15)
display.text("Thijs den Braver", 1, 25)
display.show()

while True:

	def setVariables():
		display.fill(0)
		# Laat ff de creator en de position op het scherm zien.
		display.text("Position:" + ' ' + str(number), 1, 0)
		display.text('Made By:', 1, 15)
		display.text("Thijs den Braver", 1, 25)
		display.show()

		if number >= 1:
			led1.on()
		else:
			led1.off()

		if number >= 2:
			led2.on()
		else:
			led2.off()

		if number >= 3:
			led3.on()
		else:
			led3.off()

		if number >= 4:
			led4.on()
		else:
			led4.off()

		servo.duty(122 - (number*23))
		time.sleep(.25)
		return;
	# Doet de position iets omhoog als het kan.
	if not buttonup.value():
		number = number + 1
		if number > 4:
			number = 4
		
		setVariables()

		
	# Doet de position iets omlaag als het kan.
	if not buttondown.value():
		number = number - 1
		if number < 0:
			number = 0

		setVariables()



