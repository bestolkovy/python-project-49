# Логика для игры even
from random import randint


MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'


# upd Вынесли проверку на четность в отдельную функцию
def is_even(argument):
    return argument % 2 == 0


def meat():
    argument = randint(1, 100)
    if is_even(argument):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return argument, right_answer
