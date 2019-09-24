import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_state = GPIO.input(17)
lastX = GPIO.input(23)
lastY = GPIO.input(24)

mode = 0

responses = ["woooah", "Hello there", "I need to sleep", "K."]
frequencies = [261.63, 293.66, 329.63, 349.23]
emote = [":|", ":)", ":(", ">:("]

while True:
    switch_state = GPIO.input(17)
    if switch_state == False and switch_state != last_state:
        mode = (mode + 1) % 3
        print("mode: " + str(mode))
        last_state = False
        time.sleep(0.5)

    if switch_state == True and switch_state != last_state:
        mode = (mode + 1) % 3
        print("mode: " + str(mode))
        last_state = True
        time.sleep(0.5)
    

    move1 = (0,1)
    move2 = (0,0)
    move3 = (1,0)
    
    joystickX = GPIO.input(23)
    joystickY = GPIO.input(24)
    
    # determine current state of joystick
    if (joystickX, joystickY) == move1:
        curr_mov = 1
    elif (joystickX, joystickY) == move2:
        curr_mov = 2
    elif (joystickX, joystickY) == move3:
        curr_mov = 3
    else:
        curr_mov = 0
    
    # mode 0 (displays random phrases)
    if mode == 0:
        button_state = GPIO.input(15)
        if button_state == False:
            print(responses[curr_mov])
            time.sleep(0.2)
    # mode 1 (plays C, D, E, and F notes)
    elif mode == 1:
        button_state = GPIO.input(15)
        if button_state == False:
            os.system('play -nq -t alsa synth {} sine {}'.format(500, frequencies[curr_mov]))
            # os.system('beep -f %s -l %s' % (frequencies[curr_mov],500))
            time.sleep(0.2)
    # mode 2 (displays emoticons)
    elif mode == 2:
        button_state = GPIO.input(15)
        if button_state == False:
            print(emotes[curr_mov])
            time.sleep(0.2)

