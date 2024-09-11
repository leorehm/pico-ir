import time
from machine import Pin
from ir_rx.nec import SAMSUNG

led = Pin("LED", Pin.OUT)

def callback(data, addr, ctrl):
    if data < 0:
        print("Repeat code")
    else:
        print("Data {:02x} Address {:04x}".format(data, addr))

nec = SAMSUNG(Pin(16, Pin.IN), callback)

while True:
    time.sleep_ms(500)
    led.toggle()