from setup import *

NUM_DRUMS = 3
NUM_PIANO = 7

class Instrument(object):

    def __init__(self):
        self.loop = False
        self.condition = Condition()
        self.stop_event = Event()
        self.live_thread_1 = None
        self.is_looping = False

    def loop_instrument(self, number):
        pass

    def live_loop(self, condition, stop_event, number):
        while not stop_event.is_set():
            with condition:
                condition.notifyAll() #Message to threads
            self.loop_instrument(number)

    def start_loop(self, number):
        self.stop_event = Event()
        self.live_thread = Thread(name='play_loop',
                                    target=self.live_loop,
                                    args=(self.condition,
                                          self.stop_event,
                                          number))
        self.live_thread.start()
        self.is_looping = True

    def stop_loop(self):
        self.stop_event.set()
        self.is_looping = False



class Piano(Instrument):

    def __init__(self):
        super().__init__()
        self.sc = scale(E4, MINOR)
        self.num = NUM_PIANO

    def loop_instrument(self, number):

        use_synth(PIANO)

        if number == 0:
            play_pattern_timed(scale(C3, MAJOR), 0.500, release = 0.1)


class Drum(Instrument):

    def __init__(self):
        super().__init__()
        self.num = NUM_DRUMS

    def loop_instrument(self, number):

        # first drum sample
        if number == 0:
            sample(DRUM_HEAVY_KICK)
            sleep(.3)
            sample(DRUM_HEAVY_KICK)
            sleep(.3)
            sample(DRUM_SNARE_HARD)
            sample(DRUM_CYMBAL_PEDAL)
            sleep(.3)
            sample(DRUM_HEAVY_KICK)
            sleep(.3)
            sample(DRUM_HEAVY_KICK)
            sleep(.3)
            sample(DRUM_SNARE_HARD)
            sample(DRUM_CYMBAL_PEDAL)
            sleep(.3)
            sample(DRUM_HEAVY_KICK)
            sleep(.6)

        # second drum sample
        elif number == 1:
            sample(DRUM_BASS_SOFT)
            sleep(.6)
            sample(DRUM_SNARE_SOFT)
            sample(DRUM_CYMBAL_PEDAL)
            sleep(.6)
            sample(DRUM_BASS_SOFT)
            sleep(.6)
            sample(DRUM_SNARE_SOFT)
            sample(DRUM_CYMBAL_PEDAL)
            sleep(.6)

        # third drum sample
        elif number == 2:
            sample(DRUM_BASS_SOFT)
            sleep(1.2)
            sample(DRUM_SNARE_SOFT)
            sample(DRUM_CYMBAL_PEDAL)
            sleep(1.2)
