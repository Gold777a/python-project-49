#!/usr/bin/env python3

import prompt
from brain_games.games.gcd import welcome_gcd


def welcome_all():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    welcome_gcd()
    print('Congratulations, {0}'.format(name))


def main():
    welcome_all()


if __name__ == '__main__':
    main()
