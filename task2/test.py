from setup import *
from instruments import *

i = 0

drum = Drum()
piano = Piano()
modes = ["DRUMS_MODE", "PIANO_MODE", "place", "place"]

curr_mode = modes[0]

while True:
	command = ser.readline()

	if command:
		ser.flushInput()

		if command in change_mode_cmds:

			# switch to drums mode
			if command == DRUM_MODE:
				curr_mode = modes[0]
				i = 0

			elif command == PIANO_MODE:
				curr_mode = modes[1]
				i = 0

			print(curr_mode)

		if curr_mode is "DRUMS_MODE":
			if command == BUTTON_PRESSED:

				if drum.is_looping:
					drum.stop_loop()
					print("Stop")
				else:
					drum.start_loop(i)
					print("start")
				ser.flushInput()

			# switch between drum samples
			elif command == RIGHT:
				i = (i + 1) % drum.num
				print(i)
			elif command == LEFT:
				if i == 0:
					i = drum.num - 1
				else: i -= 1
				print(i)

		elif curr_mode is "PIANO_MODE":
			if command == BUTTON_PRESSED:

				if piano.is_looping:
					piano.stop_loop()
					print("Stop")
				else:
					piano.start_loop(i)
					print("start")
				ser.flushInput()

			# switch between piano notes
			elif command == RIGHT:
				i = (i + 1) % piano.num
				print(i)
			elif command == LEFT:
				if i == 0:
					i = piano.num - 1
				else: i -= 1
				print(i)
