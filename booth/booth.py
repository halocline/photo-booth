import datetime
import time

from gpiozero import OutputDevice, Buzzer, LED

from aiy.board import Board, Led
from aiy.leds import (Leds, Pattern, PrivacyLed, RgbLeds, Color)
from aiy.toneplayer import TonePlayer

from picamera import PiCamera

from assets.songs import jingleBells
from assets.cli_transitions import byeScreen, welcomeScreen


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
            TonePlayer(22).play(*jingleBells(6))
            board.led.state = Led.OFF

    def menu(self):
        print('Press Arcade Button to begin photo shoot.' + '\n')
        with Board() as board, Leds() as leds:
            while True:
                # pulse LED to indicate ready state
                leds.pattern = Pattern.blink(1000)
                leds.update(Leds.rgb_pattern(Color.WHITE))
                board.button.wait_for_press()
                startTime = datetime.datetime.now()
                board.led.state = Led.ON
                print('LED is on...')
                # update LED to green indicating shoot is live
                leds.update(Leds.rgb_on((107, 255, 0)))
                self.shoot()
                leds.pattern = Pattern.blink(1000)
                leds.update(Leds.rgb_pattern(Color.WHITE))
                print('Press Arcade Button to start again' + '\n' + 'OR....' +
                      '\n' + 'Press and HOLD the Arcade Button for 5 seconds to quit')
                board.button.wait_for_press()
                pressTime = datetime.datetime.now()
                board.button.wait_for_release()
                releaseTime = datetime.datetime.now()
                board.led.state = Led.OFF
                print('OFF')

                pressDuration = releaseTime - pressTime
                sessionDuration = releaseTime - startTime
                if pressDuration.seconds >= 5:
                    leds.update(Leds.rgb_on(Color.PURPLE))
                    print('Photo booth session ran for ' +
                          str(sessionDuration.seconds) + ' seconds')
                    time.sleep(3)
                    TonePlayer(22).play(*[
                        'D5e',
                        'rq',
                        'C5e',
                        'rq',
                        'Be',
                        'rq',
                        'Be',
                        'C5e',
                        'D5e'
                    ])
                    break
                print('Done')

    def shoot(self):
        with PiCamera() as camera, Leds() as leds:
            countdown = self.initial_timing
            shots_remaining = self.num_shots

            # Configure camera
            camera.resolution = (1640, 922)  # Full Frame, 16:9 (Camera v2)
            # camera.start_preview()
            leds.update(Leds.privacy_on())

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
                camera.capture(
                    './photos/photobooth_' + str(datetime.datetime.now()) + '.jpg')
                shots_remaining -= 1
            print('\n' + 'You looked FABULOUS!!!' + '\n')
            time.sleep(3)
            # Stop preview
            # camera.stop_preview()
            leds.update(Leds.privacy_on())

    def bye(self):
        byeScreen()
