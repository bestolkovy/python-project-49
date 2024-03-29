import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def answer():
    number = randint(1, 347)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if answer == right_answer(number):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer(number)}'.")
        return False
