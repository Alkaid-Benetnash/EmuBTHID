evdev_xkb_map = {
    94: 100,           # Non-US \	NonUS Backslash
    49: 53,            # `	Grave
    10: 30,            # 1
    11: 31,            # 2
    12: 32,            # 3
    13: 33,            # 4
    14: 34,            # 5
    15: 35,            # 6
    16: 36,            # 7
    17: 37,            # 8
    18: 38,            # 9
    19: 39,            # 0
    20: 45,            # -	Minus
    21: 46,            # =	Equals
    22: 42,            # Delete
    23: 43,            # Tab
    24: 20,            # Q
    25: 26,            # W
    26: 8,             # E
    27: 21,            # R
    28: 23,            # T
    29: 28,            # Y
    30: 24,            # U
    31: 12,            # I
    32: 18,            # O
    33: 19,            # P
    34: 47,            # [	Left Bracket
    35: 48,            # ]	Right Bracket
    51: 49,            # \	Backslash
    36: 40,            # Enter
    66: 57,            # Caps Lock
    38: 4,             # A
    39: 22,            # S
    40: 7,             # D
    41: 9,             # F
    42: 10,            # G
    43: 11,            # H
    44: 13,            # J
    45: 14,            # K
    46: 15,            # L
    47: 51,            # ;	Semicolon
    48: 52,            # '	Quote
    50: 225,           # Left Shift
    52: 29,            # Z
    53: 27,            # X
    54: 6,             # C
    55: 25,            # V
    56: 5,             # B
    57: 17,            # N
    58: 16,            # M
    59: 54,            # ,	Comma
    60: 55,            # .	Period
    61: 56,            # /	Slash
    62: 229,           # Right Shift
    64: 226,           # Left Alt
    37: 224,           # Left Control
    65: 44,            # Space
    105: 228,          # Right Control
    108: 230,          # Right Alt
    133: 227,          # Left GUI
    134: 231,          # Right GUI
    9: 41,             # Escape
    67: 58,            # F1
    68: 59,            # F2
    69: 60,            # F3
    70: 61,            # F4
    71: 62,            # F5
    72: 63,            # F6
    73: 64,            # F7
    74: 65,            # F8
    75: 66,            # F9
    76: 67,            # F10
    95: 68,            # F11
    96: 69,            # F12
    107: 70,           # Print Screen
    78: 71,            # Scroll Lock
    127: 72,           # Pause
    118: 73,           # Insert
    110: 74,           # Home
    112: 75,           # Page Up
    119: 76,           # Delete Forward
    115: 77,           # End
    117: 78,           # Page Down
    111: 82,           # Up
    113: 80,           # Left
    116: 81,           # Down
    114: 79,           # Right
    77: 83,            # KP NumLock
    106: 84,           # KP /	KP Divide
    63: 85,            # KP *	KP Multiply
    82: 86,            # KP -	KP Subtract
    79: 95,            # KP 7
    80: 96,            # KP 8
    81: 97,            # KP 9
    86: 87,            # KP +	KP Add
    83: 92,            # KP 4
    84: 93,            # KP 5
    85: 94,            # KP 6
    87: 89,            # KP 1
    88: 90,            # KP 2
    89: 91,            # KP 3
    104: 88,           # KP Enter
    90: 98,            # KP 0
    91: 99,            # KP .	KP Point
    125: 103,          # KP =	KP Equals
    191: 104,          # F13
    192: 105,          # F14
    193: 106,          # F15
    194: 107,          # F16
    195: 108,          # F17
    196: 109,          # F18
    197: 110,          # F19
    198: 111,          # F20
    199: 112,          # F21
    200: 113,          # F22
    201: 114,          # F23
    202: 115,          # F24
}

modkeys = {
    231: 1 << 7,            # KEY_RIGHTMETA
    230: 1 << 6,            # KEY_RIGHTALT
    229: 1 << 5,            # KEY_RIGHTSHIFT
    228: 1 << 4,            # KEY_RIGHTCTRL
    227: 1 << 3,            # KEY_LEFTMETA
    226: 1 << 2,            # KEY_LEFTALT
    225: 1 << 1,            # KEY_LEFTSHIFT
    224: 1 << 0             # KEY_LEFTCTRL
}