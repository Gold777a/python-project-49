#!/usr/bin/env python3

import prompt
from brain_games.games.gcd import welcome_gcd


def welcome_all():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
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
