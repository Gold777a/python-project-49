#!/usr/bin/env python3

from brain_games.games.gcd import welcome_gcd
from brain_games.scripts.brain_all import single


def welcome_all():
    name = single()
    print('Find the greatest common divisor of given numbers.')
    rez = welcome_gcd()
    if rez == 0:
        print('Let\'s try again, {0}!'.format(name))
    else:
        print('Congratulations, {0}!'.format(name))


def main():
    welcome_all()


if __name__ == '__main__':
    main()
