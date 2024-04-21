# Логика для игры Простое число
from random import randint

MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# upd Выделили проверку на простоту в отдельную функцию
def is_prime(argument):
    for i in range(2, int(argument ** 0.5 + 1)):
        if argument % i == 0:
            return False
    return True


def get_question_and_answer():
    MIN_VALUE = 1
    MAX_VALUE = 100
    argument = randint(MIN_VALUE, MAX_VALUE)
    if is_prime(argument):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return argument, right_answer
