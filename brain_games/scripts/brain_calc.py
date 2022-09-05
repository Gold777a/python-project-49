#!/usr/bin/env python3

from brain_games.games.calc import welcome_calc
from brain_games.scripts.brain_all import single


def welcome_all():
    name = single()
    print('What is the result of the expression?')
    rez = welcome_calc()
    if rez == 0:
        print('Let\'s try again, {0}!'.format(name))
    else:
        print('Congratulations, {0}!'.format(name))


def main():
    welcome_all()


if __name__ == '__main__':
    main()
