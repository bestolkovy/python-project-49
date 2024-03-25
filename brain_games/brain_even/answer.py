# Основной скрипт brain_games/scripts/brain_even.
# Проверка ответа на вопрос о четности в модулe brain_games/answer
# Подсчет с финальным ответом в модуле brain_games/count.py.
from random import randint
import prompt

# Функция проверки на четность
def check_even(num):
    return "yes" if num % 2 == 0 else "no"

# Вывод случайного числа и ответ игрока четное оно или нет. Проверка ответа.
def answer():
    number = randint(1, 347)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if answer == check_even(number):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{check_even(number)}'.")
        return False
