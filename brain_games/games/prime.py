# Логика для игры Простое число
from random import randint

MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(argument):
    for i in range(2, int(argument ** 0.5 + 1)):
        return argument % i == 0


def meat():
    argument = randint(1, 100)
    if is_prime(argument):
        right_anser = 'no'
    else:
        right_anser = 'yes'    
    return argument, right_anser
