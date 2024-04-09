# Логика для игры Простое число
from random import randint

MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def meat():
    num = randint(1, 100)
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return num, 'noo'
    return num, 'yes'
