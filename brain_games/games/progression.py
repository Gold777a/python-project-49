from random import randint
import prompt
import sys


def welcome_progression():
    cnt = 3
    while cnt > 0:
        start = randint(2, 10)
        step = randint(2, 10)
        stop = randint(5, 12)
        rez = []

        for i in range(start, step*12, step):
            if len(rez) < stop:
                rez.append(i)

        choice = randint(1, len(rez))
        good_value = rez[choice - 1]
        rez[choice - 1] = '..'

        print('Question:', *rez, sep=' ')

        rez = prompt.string('Your answer: ')

        if good_value == int(rez):
            print('Correct!')
            cnt -= 1
        else:
            print('{0} is wrong answer ;(. Correct answer was {1}.'.format(rez, good_value))
            sys.exit()
