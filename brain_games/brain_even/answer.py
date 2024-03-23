from random import randint
import prompt


def check_even(num):
    return "yes" if num % 2 == 0 else "no"


def answer():
    number = randint(0, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if answer == check_even(number):
        return True
    else:
        return False

