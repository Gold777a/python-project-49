from random import randint
import prompt
import sys


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def welcome_prime():
    cnt = 3
    while cnt > 0:
        number = randint(2, 500)
        good_value = is_prime(number)
        print('Question:', number)

        rez = prompt.string('Your answer: ')

        if (rez == 'yes' and good_value) or (rez == 'no' and not good_value):
            print('Correct!')
            cnt -= 1
        else:
            print('{0} is wrong answer ;(. Correct answer was {1}.'.format(rez, good_value))
            return 0
