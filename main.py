from machine import Pin
import network as nt

import time
l=Pin(4, Pin.OUT)
l.value(1)
l2=Pin(33, Pin.OUT)

while True :
    l.value(0)
    time.sleep(0.5)
    l.value(1)
    time.sleep(0.5)
    break
l.value(0)