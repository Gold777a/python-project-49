import random
import prompt


def welcome_calc():
    cnt = 3
    while cnt > 0:
        value1 = random.randint(1, 30)
        value2 = random.randint(1, 30)
        sig = random.randint(1, 3)
        if sig == 1:
            good_value = value1 + value2
            print('Question: {0} + {1}'.format(value1, value2))
        elif sig == 2:
            good_value = value1 - value2
            print('Question: {0} - {1}'.format(value1, value2))
        else:
            good_value = value1 * value2
            print('Question: {0} * {1}'.format(value1, value2))

        rez = prompt.string('Your answer: ')

        if good_value == int(rez):
            print('Correct!')
            cnt -= 1
        else:
            print('{0} is wrong answer ;(. Correct answer was {1}.'.format(rez, good_value))
            return 0
