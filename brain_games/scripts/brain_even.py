#!/usr/bin/env python3
from random import randint
import prompt
#from brain_games.scripts.brain_games import main


#main()


number = randint(0, 100)


def check_even():
    return "yes" if number % 2 == 0 else "no"


print('Answer "yes" if the number is even, otherwise answer "no".')
print(f'Question: {number}')
answer = prompt.string('Your answer: ')
if answer == check_even():
    print('you are smart, mazafaka')
else:
    print('gandon')


