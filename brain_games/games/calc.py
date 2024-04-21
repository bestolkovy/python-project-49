# Логика для игры calc
from random import randint, choice
import operator


MANUAL = 'What is the result of the expression?'


def get_question_and_answer():
    MIN_VALUE = 1
    MAX_VALUE = 50
    first_num = randint(MIN_VALUE, MAX_VALUE)
    second_num = randint(MIN_VALUE, MAX_VALUE)
    list_op = (('+', operator.add), ('-', operator.sub), ('*', operator.mul))
    operand = choice(list_op)
    argument = f'{first_num} {operand[0]} {second_num}'
    right_answer = str(operand[1](first_num, second_num))
    return argument, right_answer
