#!/usr/bin/env python3

import prompt
from brain_games.games.even import welcome_even


def welcome_new():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rez = welcome_even()
    if rez == 0:
        print('Let\'s try again, {0}!'.format(name))
    else:
        print('Congratulations, {0}!'.format(name))


def main():
    welcome_new()


if __name__ == '__main__':
    main()
