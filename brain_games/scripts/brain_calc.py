#!/usr/bin/env python3

import prompt
from brain_games.games.calc import welcome_calc

def welcome_all():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('What is the result of the expression?')
    welcome_calc()
    print('Congratulations, {0}'.format(name))

def main():
    welcome_all()


if __name__ == '__main__':
    main()
