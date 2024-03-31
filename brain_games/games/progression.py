# Логика для игры Арифметическая прогрессия
from random import randint


MANUAL = 'What number is missing in the progression?'


def meat():
    start = randint(2, 45)
    step = randint(2, 8)
    progression = [start + i * step for i in range(10)]
    random_num = randint(0, 9)
    right_answer = str(progression[random_num])
    progression[random_num] = '..'
    argument = ' '.join(map(str, progression))
    return argument, right_answer
