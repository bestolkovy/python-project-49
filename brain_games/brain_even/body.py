# Основной скрипт brain_games/scripts/brain_even.
# Проверка ответа на вопрос о четности в модулe brain_games/answer
# Подсчет с финальным ответом в модуле brain_games/count.py.
from random import randint
import brain_games.cli
import brain_games.scripts.brain_games
from brain_games.brain_even.skeleton import count, answer, test_del


# Правильный ответ. Переменные argument, right_answ - для всех игр разные, но названия одинаковые.
def right_answer():
    argument = randint(1, 347)
    right_answ = 'no'
    if argument % 2 == 0:
        right_answ = "yes"
    return argument, right_answ


def zadanie():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


brain_games.scripts.brain_games.main()
name = brain_games.cli.welcome_user()
print(zadanie())

answer(right_answer(), name)