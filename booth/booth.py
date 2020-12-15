#!/usr/bin/env python3
# booth.py
#

from gpiozero import OutputDevice, Buzzer, LED


class Booth:
    def __init__(self):
        self._name = 'Photo booth'

    def close(self):
        self._name = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()


def main():
    with Booth() as booth:
        print('hello world')
        print('Photo booth\'s name: ' + booth._name)


if __name__ == '__main__':
    main()
