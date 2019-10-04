import serial
import platform
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
BELLS_MODE = b'2\r\n'
SAMPLER_MODE = b'3\r\n'
BASS_MODE = b'4\r\n'

change_mode_cmds = {DRUM_MODE, PIANO_MODE, BELLS_MODE, SAMPLER_MODE, BASS_MODE}

# grab the correct serial port for Mac or Linux
if platform.system() == 'Darwin':
    ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)
elif platform.system() == 'Linux':
    ser = serial.Serial('/dev/ttyUSB0', 9600)
