# Copyright by Thijs den Braver 2017

# PIN LAYOUT VOOR DE WEMOS:
# scherm = pin 5 & 4

# Import alle dependencies.
import machine
import framebuf
from machine import Pin, PWM, I2C
import time
import ssd1306  
import sys

   
# Defineer alle hardware
i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(128, 32, i2c)


display.fill(0)

# Hier defineer ik het whatsapp logo in 32 rijen. Dit doe ik omdat als ik het in 1 array doe een wemos gaat zeuren dat het te groot is.
row1 =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
row2 =  [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
row3 =  [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
row4 =  [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
row5 =  [0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0]
row6 =  [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0]
row7 =  [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0]
row8 =  [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0]
row9 =  [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0]
row10 = [0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0]
row11 = [0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0]
row12 = [0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]
row13 = [0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]
row14 = [0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]
row15 = [0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]
row16 = [0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]
row17 = [0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]
row18 = [0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]
row19 = [0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0]
row20 = [0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0]
row21 = [0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0]
row22 = [0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0]
row23 = [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0]
row24 = [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0]
row25 = [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0]
row26 = [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0]
row27 = [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0]
row28 = [0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0]
row29 = [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0]
row30 = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
row31 = [0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
row32 = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Laat ff de creator op het scherm zien.
display.text('Whatsapp', 1, 0)
display.text('Thijs', 1, 15)
display.text("06-19991***", 1, 25)
display.show()


# En dan hier 32 keer hetzelfde alleen omdat mijn wemos de array anders te groot vond.
for digit in range(0, len(row1)):
	display.pixel((digit + 96), 1, row1[digit])

for digit in range(0, len(row2)):
	display.pixel((digit + 96), 2, row2[digit])

for digit in range(0, len(row3)):
	display.pixel((digit + 96), 3, row3[digit])

for digit in range(0, len(row4)):
	display.pixel((digit + 96), 4, row4[digit])

for digit in range(0, len(row5)):
	display.pixel((digit + 96), 5, row5[digit])

for digit in range(0, len(row6)):
	display.pixel((digit + 96), 6, row6[digit])

for digit in range(0, len(row7)):
	display.pixel((digit + 96), 7, row7[digit])

for digit in range(0, len(row8)):
	display.pixel((digit + 96), 8, row8[digit])

for digit in range(0, len(row9)):
	display.pixel((digit + 96), 9, row9[digit])

for digit in range(0, len(row10)):
	display.pixel((digit + 96), 10, row10[digit])



for digit in range(0, len(row11)):
	display.pixel((digit + 96), 11, row11[digit])

for digit in range(0, len(row12)):
	display.pixel((digit + 96), 12, row12[digit])

for digit in range(0, len(row13)):
	display.pixel((digit + 96), 13, row13[digit])

for digit in range(0, len(row14)):
	display.pixel((digit + 96), 14, row14[digit])

for digit in range(0, len(row15)):
	display.pixel((digit + 96), 15, row15[digit])

for digit in range(0, len(row16)):
	display.pixel((digit + 96), 16, row16[digit])

for digit in range(0, len(row17)):
	display.pixel((digit + 96), 17, row17[digit])

for digit in range(0, len(row18)):
	display.pixel((digit + 96), 18, row18[digit])

for digit in range(0, len(row19)):
	display.pixel((digit + 96), 19, row19[digit])

for digit in range(0, len(row20)):
	display.pixel((digit + 96), 20, row20[digit])



for digit in range(0, len(row21)):
	display.pixel((digit + 96), 21, row21[digit])

for digit in range(0, len(row22)):
	display.pixel((digit + 96), 22, row22[digit])

for digit in range(0, len(row23)):
	display.pixel((digit + 96), 23, row23[digit])

for digit in range(0, len(row24)):
	display.pixel((digit + 96), 24, row24[digit])

for digit in range(0, len(row25)):
	display.pixel((digit + 96), 25, row25[digit])

for digit in range(0, len(row26)):
	display.pixel((digit + 96), 26, row26[digit])

for digit in range(0, len(row27)):
	display.pixel((digit + 96), 27, row27[digit])

for digit in range(0, len(row28)):
	display.pixel((digit + 96), 28, row28[digit])

for digit in range(0, len(row29)):
	display.pixel((digit + 96), 29, row29[digit])

for digit in range(0, len(row20)):
	display.pixel((digit + 96), 30, row30[digit])



for digit in range(0, len(row31)):
	display.pixel((digit + 96), 31, row31[digit])

for digit in range(0, len(row32)):
	display.pixel((digit + 96), 32, row32[digit])

# De code die zorgt dat je ook kan zien wat er gebeurd.
display.show()





