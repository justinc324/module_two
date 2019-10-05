# Music Box
Hi! Thanks for checking this out. While most digital instruments require some baseline knowledge of music to make something decent, I wanted to make something nice and simple anybody could pick up and play! My music box allows a user to create and stack a few different loops and play samples on top of them! In particular there are drum, piano, and bell synethizer loops to pick from (around 4-5 of each), and there are ~7 bass samples and ~6 audio samples to play with. Operation is pretty simple - the switch controls the instrument the user is currently on, the joystick can be flicked left/right to switch between sample, and the button is used to start/stop loops and play samples. Requires a headset or speakers, as well as a power connection.

## Setup

### Necessary Hardware
- Raspberry Pi Model 3 B+
- Espressif ESP32 DevKitC
- Analog joystick 
- SPST switch (soldered)
- Momentary push button (soldered)
- Breadboard
- LOTS of various male/female wires
- 10M Ohm resistor

### Software to Install

Unfortunately, this music box requires a LOT of dependencies to run. See below.

#### Arduino 
I used the [Arduino IDE](https://www.arduino.cc/en/main/software) to flash the Espressif ESP32 DevKitC with the code here. Pretty straight forward. 

#### Sonic-Pi Dev

As of writing this, the standard Sonic-Pi 3.1 that ships with Raspbian and available on the website will NOT work with this setup. Sonic Pi requires a GUI to run, but another library we use (Sonic-Pi-Tool) to run it headless does not play nicely with the current version of Sonic Pi, so you will need to download the latest development version. [Instructions here.](https://in-thread.sonic-pi.net/t/building-sp3-2dev-from-source-on-a-pi4-edit-addendum-added/2645) (Follow them to a T!)

#### Sonic-Pi-Tool

- Go the the `src` directory that you created in the previous step and download the [Sonic Pi Tool](https://github.com/emlyn/sonic-pi-tool). This is a script that allows us to use Sonic Pi without a GUI.

- We are going to need to make a *slight* change to the source code in order to make this points to the dev version of Sonic Pi we just installed. After installing the dependencies and cloning the repo, navigate to the script `sonic-pi-tool.py`, and go to line 284. Replace the first element of that tuple with the following: `/home/{your username on raspberry pi}/src/sonic-pi/`. Here, we are just telling Sonic-Pi-Tool to look for our dev version of Sonic-Pi to run. Make sure you update the executable and run `chmod -x sonic-pi-tool.py` after editing the source code.

#### Python-Sonic

Finally, we need to install this wonderful little tool called [Python-Sonic](https://github.com/gkvoelkl/python-sonic)! Luckily, we don't need to do anything crazy with this one. `pip3 install python-sonic` should do the trick.

### Running it

In order to run this, you will need to execute these commands in this order, in three **separate** processes:
1. `sonic-pi-tool logs` <-- Starts the logs for the Sonic Pi server.
2. `sonic-pi-tool start-server` <-- Starts the Sonic Pi server.
3. `python3 player.py` <-- Starts our music player.

I'd recommend putting these commands together into a script for easy running. Unfortunately I was not able to get my script to run on boot, so as of now I need to SSH into my music box to start the script.
