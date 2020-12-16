from booth.booth import Booth


event_name = 'Glissmann\'s Ugly Sweater Party 2020'


def main():
    with Booth(event_name, 4, 3) as booth:
        booth.startup()
        booth.welcome()
        # booth.menu()
        # booth.shoot()
        # booth.bye()


if __name__ == '__main__':
    main()
