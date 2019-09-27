import serial

ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 9600)
button_pressed = b'1'

while True:
	command = ser.read()
	if command:
		ser.flushInput()
		if command == button_pressed:
			print("pressed!")
