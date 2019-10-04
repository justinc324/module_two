from setup import *

NUM_DRUMS = 3
NUM_PIANO = 5
NUM_BASS = 6
NUM_SAMPLE = 6

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

class Sampler(Instrument):

    def __init__(self):
        super().__init__()
        self.num = NUM_SAMPLE

    def play(self, number):

        if number == 0:
            sample(AMBI_CHOIR)

        elif number == 1:
            sample(AMBI_DARK_WOOSH)

        elif number == 2:
            sample(AMBI_DRONE)

        elif number == 3:
            sample(AMBI_GLASS_HUM)

        elif number == 4:
            sample(AMBI_LUNAR_LAND)

        elif number == 5:
            sample(AMBI_SWOOSH)

class Bass(Instrument):

    def __init__(self):
        super().__init__()
        self.num = NUM_BASS

    def play(self, number):
        if number == 0:
            sample(BASS_DNB_F)

        elif number == 1:
            sample(BASS_DROP_C)

        elif number == 2:
            sample(BASS_HARD_C)

        elif number == 3:
            sample(BASS_HIT_C)

        elif number == 4:
            sample(BASS_THICK_C)

        elif number == 5:
            sample(BASS_VOXY_C)


class Piano(Instrument):

    def __init__(self):
        super().__init__()
        self.sc = scale(C3, MAJOR)
        self.num = NUM_PIANO

    def loop_instrument(self, number):

        use_synth(PIANO)

        # plays the scale up
        if number == 0:
            play_pattern_timed(self.sc, 0.343857, release = 0.1)

        # plays a I-V-vi-VI chord progression
        elif number == 1:
            play(chord(self.sc[0], MAJOR))
            sleep(.6)
            play(chord(self.sc[5], MINOR))
            sleep(.6)
            play(chord(self.sc[3], MAJOR))
            sleep(.6)
            play(chord(self.sc[4], MAJOR))
            sleep(.6)

        # plays an major arpeggio
        elif number == 2:
            play_pattern_timed(chord(self.sc[0], MAJOR), 0.2)

        # a differnt arpeggio
        elif number == 3:
            play_pattern_timed(chord(self.sc[4], MAJOR), 0.2)

        # plays a minor arpeggio
        elif number == 4:
            play_pattern_timed(chord(self.sc[5], MINOR), 0.6)

class BellSynth(Piano):

    def __init__(self):
        super().__init__()

    def loop_instrument(self, number):

        use_synth(PRETTY_BELL)

        # plays the scale up
        if number == 0:
            play_pattern_timed(self.sc, 0.343857, release = 0.1)

        # plays a I-V-vi-VI chord progression
        elif number == 1:
            play(chord(self.sc[0], MAJOR))
            sleep(.6)
            play(chord(self.sc[5], MINOR))
            sleep(.6)
            play(chord(self.sc[3], MAJOR))
            sleep(.6)
            play(chord(self.sc[4], MAJOR))
            sleep(.6)

        # plays an major arpeggio
        elif number == 2:
            play_pattern_timed(chord(self.sc[0], MAJOR), 0.2)

        # a differnt arpeggio
        elif number == 3:
            play_pattern_timed(chord(self.sc[4], MAJOR), 0.2)

        # plays a minor arpeggio
        elif number == 4:
            play_pattern_timed(chord(self.sc[5], MINOR), 0.6)

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
