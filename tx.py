import time
import network
from machine import Pin
from ir_tx.nec import NEC

class SamsungTransmitter(NEC):
    
    def __init__(self):
        NEC.samsung = True

NEC.samsung = True

led = Pin("LED", Pin.OUT)
nec = NEC(Pin(17, Pin.OUT, value = 0))

addr = 0x0707

commands = {
    "KEY_POWER": 0xe6,
    "KEY_SOURCE": 0x01,
    "KEY_SETTINGS": 0x1a,
    "KEY_UP": 0x60,
    "KEY_DOWN": 0x61,
    "KEY_LEFT": 0x65,
    "KEY_RIGHT": 0x62,
    "KEY_ENTER": 0x68,
    "KEY_HOME": 0x79,
    "KEY_RETURN": 0x58,
    "KEY_EXIT": 0x2d,
    "KEY_VOLUMEUP": 0x07,
    "KEY_VOLUMEDOWN": 0x0b,
    "KEY_CHANNELUP": 0x12,
    "KEY_CHANNELDOWN": 0x10,
    "KEY_BACKWARD": 0x45,
    "KEY_FORWARD": 0x48,
    "KEY_PLAY": 0x47,
    "KEY_PAUSE": 0x4a,
    "KEY_STOP": 0x46,
    "KEY_EPG": 0x4f,
    "KEY_1": 0x04,
    "KEY_2": 0x05,
    "KEY_3": 0x06,
    "KEY_4": 0x08,
    "KEY_5": 0x0d,
    "KEY_6": 0x0a,
    "KEY_7": 0x0c,
    "KEY_8": 0x0d,
    "KEY_9": 0x0e,
    "KEY_MUTE": 0x0f,
    "KEY_LIST": 0x6b
}

# nec.transmit(addr, commands["KEY_POWER"], validate = True)

lower_brightness_by_5 = [
    "SETTINGS",
    "ENTER",
    "DOWN",
    "DOWN",
    "ENTER",
    "ENTER",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "EXIT",
    "EXIT"
]

# for cmd in lower_brightness_by_5:
#     key = f"KEY_{cmd}"
#     print(f"sending {key}")

#     led.value(1)
#     nec.transmit(addr, commands[key])
#     time.sleep_ms(500)
#     led.value(0)

# print("done")

def send_key(key):
    if not commands[key]:
        print("key not found!")
        return
    
    nec.transmit(addr, commands[key])





# while True:
#     print("Enter a command to send:")
#     key = input()

#     if commands[key]:
#         print(f"Sending key { key }")
#         nec.transmit(addr, commands[key])
#         led.value(1)
#         time.sleep_ms(200)
#     else: 
#         print(f"Key { key } not found")

    
#     led.value(0)