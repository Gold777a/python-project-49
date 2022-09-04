import random
import prompt
import sys
from math import gcd


def welcome_gcd():
    cnt = 3
    while cnt > 0:
        value1 = random.randint(1, 30)
        value2 = random.randint(1, 30)
        good_value = gcd(value1, value2)
        print(f'Question: {value1} {value2}')


        rez = prompt.string('Your answer: ')

        if good_value == int(rez):
            print('Correct!')
            cnt -= 1
        else:
            print('{0} is wrong answer ;(. Correct answer was {1}.'.format(rez, good_value))
            sys.exit()