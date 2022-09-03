#!/usr/bin/env python3

import random
import prompt
import sys
from brain_games.games.even import welcome_even


def welcome_new():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    welcome_even()
    print(f'Congratulations, {name}')


def main():
    welcome_new()


if __name__ == '__main__':
    main()
