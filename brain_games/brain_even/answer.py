# Основной скрипт brain_games/scripts/brain_even.
# Проверка ответа на вопрос о четности в модулe brain_games/answer
# Подсчет с финальным ответом в модуле brain_games/count.py.
from random import randint
import prompt
import brain_games.cli
import brain_games.scripts.brain_games


# Правильный ответ
def right_answer(num):
    return "yes" if num % 2 == 0 else "no"

# Вывод случайного числа и ответ игрока четное оно или нет. Проверка ответа.
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
    

def count():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        k = answer()
        if k is False:
            print(f"Let's try again, {name}")
            break
    if i == 2 and k is True:
        print(f'Congratulations, {name}!')


brain_games.scripts.brain_games.main()
name = brain_games.cli.welcome_user()
