addr = 0x0707

commands = {
    "KEY_POWER":        0xe6,
    "KEY_SOURCE":       0x01,
    "KEY_SETTINGS":     0x1a,
    "KEY_UP":           0x60,
    "KEY_DOWN":         0x61,
    "KEY_LEFT":         0x65,
    "KEY_RIGHT":        0x62,
    "KEY_ENTER":        0x68,
    "KEY_HOME":         0x79,
    "KEY_RETURN":       0x58,
    "KEY_EXIT":         0x2d,
    "KEY_VOLUMEUP":     0x07,
    "KEY_VOLUMEDOWN":   0x0b,
    "KEY_CHANNELUP":    0x12,
    "KEY_CHANNELDOWN":  0x10,
    "KEY_BACKWARD":     0x45,
    "KEY_FORWARD":      0x48,
    "KEY_PLAY":         0x47,
    "KEY_PAUSE":        0x4a,
    "KEY_STOP":         0x46,
    "KEY_EPG":          0x4f,
    "KEY_1":            0x04,
    "KEY_2":            0x05,
    "KEY_3":            0x06,
    "KEY_4":            0x08,
    "KEY_5":            0x0d,
    "KEY_6":            0x0a,
    "KEY_7":            0x0c,
    "KEY_8":            0x0d,
    "KEY_9":            0x0e,
    "KEY_MUTE":         0x0f,
    "KEY_LIST":         0x6b
}

scripts = {
    "change_brightness": [
        "KEY_SETTINGS",
        "KEY_ENTER",
        "KEY_DOWN",
        "KEY_DOWN",
        "KEY_ENTER",
        "KEY_ENTER",
        "&DIR_KEYS&",
        "KEY_EXIT",
        "KEY_EXIT"
    ]
}

