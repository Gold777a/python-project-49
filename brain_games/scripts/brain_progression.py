#!/usr/bin/env python3

import prompt
from brain_games.games.progression import welcome_progression


def welcome_all():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('What number is missing in the progression?')
    rez = welcome_progression()
    if rez == 0:
        print('Let\'s try again, {0}!'.format(name))
    else:
        print('Congratulations, {0}!'.format(name))


def main():
    welcome_all()


if __name__ == '__main__':
    main()
