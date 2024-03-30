# Логика для игры calc
from random import randint, choice
import operator


MANUAL = 'What is the result of the expression?'


def meat():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    list_op = (('+', operator.add), ('-', operator.sub), ('*', operator.mul))
    operand = choice(list_op)
    argument = f'{first_num} {operand[0]} {second_num}'
    right_answer = str(operand[1](first_num, second_num))
    return argument, right_answer
