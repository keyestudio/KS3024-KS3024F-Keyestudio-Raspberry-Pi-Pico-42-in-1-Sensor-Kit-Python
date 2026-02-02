'''
 * Keyestudio 42 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 38
 * ADXL345
 * http://www.keyestudio.com
'''
from machine import Pin
import time
from ADXL345 import adxl345

scl = Pin(21)
sda = Pin(20)
bus = 0
snsr = adxl345(bus, scl, sda)
while True:
    x,y,z = snsr.readXYZ()
    print('x:',x,'y:',y,'z:',z,'uint:mg')
    time.sleep(0.1)