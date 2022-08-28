#!/usr/bin/env python3

import random
import prompt


def welcome_new():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for j in range(3):
        dig = random.randint(1, 100)
        print(f'Question: {dig}')
        rez = prompt.string('Your answer: ')
        if (dig % 2 == 0 and rez == 'yes') or (dig % 2 != 0 and rez == 'no'):
            print('Correct!')
        else:
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            exit()
    print(f'Congratulations, {name}')


def main():
    welcome_new()


if __name__ == '__main__':
    main()
