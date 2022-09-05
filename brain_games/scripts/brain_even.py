#!/usr/bin/env python3

from brain_games.games.even import welcome_even
from brain_games.scripts.brain_all import single


def welcome_new():
    name = single()
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
