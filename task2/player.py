from setup import *
from instruments import *

i = 0

drum = Drum()
piano = Piano()
bells = BellSynth()
bass = Bass()
sampler = Sampler()
modes = ["DRUMS_MODE", "PIANO_MODE", "BELLS_MODE", "SAMPLER_MODE", "BASS_MODE"]

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

			elif command == BELLS_MODE:
				curr_mode = modes[2]
				i = 0

			elif command == SAMPLER_MODE:
				curr_mode = modes[3]
				i = 0

			elif command == BASS_MODE:
				curr_mode = modes[4]
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

			# switch between piano samples
			elif command == RIGHT:
				i = (i + 1) % piano.num
				print(i)
			elif command == LEFT:
				if i == 0:
					i = piano.num - 1
				else: i -= 1
				print(i)

		elif curr_mode is "BELLS_MODE":
			if command == BUTTON_PRESSED:

				if bells.is_looping:
					bells.stop_loop()
					print("Stop")
				else:
					bells.start_loop(i)
					print("start")
				ser.flushInput()

			# switch between bell notes
			elif command == RIGHT:
				i = (i + 1) % bells.num
				print(i)
			elif command == LEFT:
				if i == 0:
					i = bells.num - 1
				else: i -= 1
				print(i)

		elif curr_mode is "SAMPLER_MODE":
			if command == BUTTON_PRESSED:

				sampler.play(i)
				print("sampler play")
				ser.flushInput()

			# switch between piano notes
			elif command == RIGHT:
				i = (i + 1) % sampler.num
				print(i)
			elif command == LEFT:
				if i == 0:
					i = sampler.num - 1
				else: i -= 1
				print(i)

		elif curr_mode is "BASS_MODE":
			if command == BUTTON_PRESSED:

				bass.play(i)
				print("bass play")
				ser.flushInput()

			# switch between piano notes
			elif command == RIGHT:
				i = (i + 1) % bass.num
				print(i)
			elif command == LEFT:
				if i == 0:
					i = bass.num - 1
				else: i -= 1
				print(i)
