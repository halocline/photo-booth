import time

from booth.booth import Booth


event_name = 'Glissmann\'s Ugly Sweater Party 2020'


def main():
    with Booth(event_name, 4, 3) as booth:
        booth.welcome()
        booth.shoot()


if __name__ == '__main__':
    main()
