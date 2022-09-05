#!/usr/bin/env python3

import prompt
from brain_games.games.prime import welcome_prime


def welcome_all():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    rez = welcome_prime()
    if rez == 0:
        print('Let\'s try again, {0}!'.format(name))
    else:
        print('Congratulations, {0}!'.format(name))


def main():
    welcome_all()


if __name__ == '__main__':
    main()
