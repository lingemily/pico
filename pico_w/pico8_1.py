import time
from machine import Pin

led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)
