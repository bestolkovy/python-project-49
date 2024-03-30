# Логика для игры НОД
from random import randint

MANUAL = "Find the greatest common divisor of given numbers."


def meat():
    a = randint(1, 100)
    b = randint(1, 100)
    argument = f'{a} {b}'
    if a > b:
        first_num = a
        second_num = b
    elif a < b:
        first_num = b
        second_num = a
    else:
        return argument, a
    while first_num != second_num:
        current_num = first_num - second_num
        if second_num > current_num:
            first_num = second_num
            second_num = current_num
        else:
            first_num = current_num
    return argument, str(first_num)
