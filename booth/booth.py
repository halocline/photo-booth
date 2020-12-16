import time

from gpiozero import OutputDevice, Buzzer, LED

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from aiy.toneplayer import TonePlayer

from audio.songs import jingleBells


def byeScreen():
    print('      .      ')
    print('      :      ')
    print('\'.___/*\___.\'')
    print('  \* \ / */  ')
    print('   >--X--<   ')
    print('  /*_/ \_*\  ')
    print('.\'   \* /   \'.')
    print('      :      ')
    print('      \'      ')
    print('\n')
    print('Merry Christmas!' + '\n' + '\n')


def welcomeScreen(name):
    print('\n' + '   *      *   ')
    print('   _\/  \/_   ')
    print('    _\/\/_    ')
    print('_\_\_\/\/_/_/_')
    print(' / /_/\/\_\ \ ')
    print('    _/\/\_    ')
    print('    /\  /\    ')
    print('   *      *   ')
    print('Season\'s Greetings!' + '\n' + '\n')
    print('Welcome to ' + name + '\n' + '\n')


class Booth:
    def __init__(self, event_name='My Photo Booth', num_shots=4, timing=3, initial_timing=5):
        self.name = event_name
        self.num_shots = num_shots
        self.timing = timing
        self.initial_timing = initial_timing

    def close(self):
        self.name = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def welcome(self):
        welcomeScreen(self.name)

    def startup(self):
        with Board() as board, Leds() as leds:
            colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN,
                      Color.BLUE, Color.PURPLE, Color.BLACK, Color.WHITE]
            board.led.state = Led.ON
            for color in colors:
                leds.update(Leds.rgb_on(color))
                time.sleep(0.25)
            print(jingleBells())
            print(jingleBells(3))
            TonePlayer(22).play(*jingleBells(5))
            board.led.state = Led.OFF

    def shoot(self):
        countdown = self.initial_timing
        shots_remaining = self.num_shots

        print('Get ready for your photo shoot!')
        time.sleep(3)
        print('Starting in')
        time.sleep(2)
        while countdown > 0:
            print(countdown)
            countdown -= 1
            time.sleep(1)
        time.sleep(1)
        print('Smile :)')
        while shots_remaining > 0:
            # if shots_remaining != self.num_shots:
            time.sleep(self.timing)
            print('*** FLASH ***')
            shots_remaining -= 1
        print('\n' + 'You looked FABULOUS!!!' + '\n')
        time.sleep(3)

    def bye(self):
        byeScreen()
