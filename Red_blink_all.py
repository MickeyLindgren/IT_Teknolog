from neopixel import NeoPixel
from machine import Pin
import time

n = 12  
p = 26  
np = NeoPixel(Pin(p, Pin.OUT), n)  

def set_color(red, green, blue):
    for i in range(n):
        np[i] = (red, green, blue)
    np.write()

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

while True:
    for _ in range(10):
        set_color(255, 0, 0)  
        time.sleep(1)  
        clear()  
        time.sleep(1)  
