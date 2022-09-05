#!/usr/bin/env python3

from brain_games.games.prime import welcome_prime
from brain_games.scripts.brain_all import single


def welcome_all():
    name = single()
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
