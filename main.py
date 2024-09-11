import time
import network
import re
from machine import Pin
from umqtt.simple import MQTTClient
from ir_tx.nec import NEC

from config.samsung_tv import *
NEC.samsung = True

# Globals
led = Pin("LED", Pin.OUT)
nec = NEC(Pin(17, Pin.OUT, value = 0))

# Functions
def main():
    blink_led(3)
    led.value(0)

    # network setup
    try:
        wlan = init_network()
    except RuntimeError as e:
        print(e)
        machine.reset()

    # mqtt setup
    try:
        client = mqtt_connect()
    except OSError as e:
        reconnect()
    
    # main loop
    while True:
        client.subscribe(b"tv-ir-key")
        client.subscribe(b"tv-ir-script")
        time.sleep(1)

def init_network(): -> network.WLAN
    # initialize network connection
    ssid = ""
    key = ""

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, key)

    # wait for connection or failure
    max_wait = 15
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print("Waiting for wifi connection")
        time.sleep(1)

    # handle connection error
    if wlan.status() != 3:
        raise RuntimeError(f"network connection failed with status {wlan.status()}")
    else:
        print(f"network connected")
        print(wlan.ifconfig())
    
    return wlan

def mqtt_connect():
    mqtt_server = "192.168.178.50"
    client_id = "pico-ir"

    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.set_callback(sub_cb)
    client.connect()

    print(f"connected to mqtt broker {mqtt_server}")

    return client

def reconnect():
    print("failed to connect to mqtt broker. reconnecting...")
    time.sleep(5)
    machine.reset()

# MQTT sub message callback 
def sub_cb(topic, msg):
    topic = topic.decode("utf-8")
    msg = msg.decode("utf-8")

    print(f"new message on topic {topic}")
    print(f"message = '{msg}'")

    try:
        if topic == "tv-ir-key":
            send_key(msg)

        elif topic == "tv-ir-script":
            # e.g. change_brightness_up_10
            if re.search(r"^change_brightness", msg):
                change_brightness(msg)
            
            else:
                run_script(msg)
    
    except Exception as e:
        # TODO: publish exception as MQTT message
        print(f"caught {type(e)}: {e}")

# Send IR keystroke
def send_key(key: str, timeout_ms: int = 550):
    assert key in commands, f"key {key} not defined"

    led.value(1)
    nec.transmit(addr, commands[key])
    time.sleep_ms(int(timeout_ms / 2))
    led.value(0)
    time.sleep_ms(int(timeout_ms / 2))

def run_script(script):
    assert script in scripts, f"script {script} not defined"

    keys = scripts[script]

    print(f"sending {len(keys)} commands from script {script}")

    for key in keys:
        send_key(key)
    
    print("done")

def change_brightness(msg):
    # parse message
    direction = re.search(r"up|down", msg).group(0)
    n = int(re.search(r"\d+$", msg).group(0))

    assert direction in ("up", "down")
    assert n > 0 and n <= 50

    if direction == "up":
        dir_key = "KEY_RIGHT" 
    else:
        dir_key = "KEY_LEFT"

    script = scripts["change_brightness"]
    keys = []

    # create a list of (key, timeout_ms) tuples 
    for key in script:
        if key == "&DIR_KEYS&":
            for i in range(0, n-1):
                keys.append((dir_key, 250))
            keys.append((dir_key, 450))
            continue
        keys.append((key, 550))

    print(f"changing tv volume by {n} using {dir_key}")

    for key in keys:
        print(key)
        send_key(key[0], key[1])

    print("done")

def blink_led(n):
    for i in range(0, n):
        led.toggle()
        time.sleep(1)

if __name__ == "__main__":
    main()