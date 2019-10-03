import serial
from psonic import *
from threading import Thread, Condition, Event

RIGHT = b'RIGHT\r\n'
LEFT = b'LEFT\r\n'
UP = b'UP\r\n'
DOWN = b'DOWN\r\n'

joystick_cmds = {RIGHT, LEFT, UP, DOWN}

BUTTON_PRESSED = b'-1\r\n'

DRUM_MODE = b'0\r\n'
PIANO_MODE = b'1\r\n'

change_mode_cmds = {DRUM_MODE, PIANO_MODE}

ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)
