# Логика для игры НОД
from random import randint

MANUAL = "Find the greatest common divisor of given numbers."


# upd Выделили проверку общего делителя в отдельную функциюл
def gcd(first_number, second_number):
    if first_number >= second_number:
        first_num = first_number
        second_num = second_number
    else:
        first_num = second_number
        second_num = first_number
    while first_num != second_num:
        current_num = first_num - second_num
        if second_num > current_num:
            first_num = second_num
            second_num = current_num
        else:
            first_num = current_num
    return first_num


def get_question_and_answer():
    MIN_VALUE = 1
    MAX_VALUE = 100
    first_number = randint(MIN_VALUE, MAX_VALUE)
    second_number = randint(MIN_VALUE, MAX_VALUE)
    argument = f'{first_number} {second_number}'
    rigt_answer = str(gcd(first_number, second_number))
    return argument, rigt_answer
