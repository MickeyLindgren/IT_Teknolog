from neopixel import NeoPixel
from machine import Pin

n = 12 # number of pixels in the Neopixel ring
p = 26 # pin atached to Neopixel ring
np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance

#Grenn = 0,128,0
#Yellow = 255,255,0
#Blue = 0,0,255
#Red = 255,0,0

np[0] = (0, 128, 0) 
np[1] = (0, 128, 0)
np[2] = (0, 128, 0)
np[3] = (0, 0, 225) 
np[4] = (0, 0 ,225)
np[5] = (0, 0, 225)
np[6] = (255, 0, 0) 
np[7] = (255, 0, 0)
np[8] = (255, 0, 0)
np[9] = (225, 225, 0) 
np[10] = (225, 225, 0)
np[11] = (225, 255, 0) 

np.write() 

