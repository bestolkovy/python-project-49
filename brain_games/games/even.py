# Логика для игры even
from random import randint

MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def meat():
    argument = randint(1, 347)
    if argument % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return argument, right_answer
