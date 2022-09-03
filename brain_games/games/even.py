#!/usr/bin/env python3

import random
import prompt
import sys


def welcome_even():
    for j in range(3):
        dig = random.randint(1, 100)
        print(f'Question: {dig}')
        rez = prompt.string('Your answer: ')
        if (dig % 2 == 0 and rez == 'yes') or (dig % 2 != 0 and rez == 'no'):
            print('Correct!')
        else:
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            sys.exit()

def main():
    welcome_even()


if __name__ == '__main__':
    main()