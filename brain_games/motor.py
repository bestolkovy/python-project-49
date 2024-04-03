# движок для всех игр
from brain_games.cli import welcome_user
from brain_games.answer import answer


def skeleton(game=''):
    print('Welcome to the Brain Games!')
    name = welcome_user()
# Функция с пустым аргументом используется только для скрипта brain-games.py:
    if game == '':
        return
# Печатаем правила:
    print(game.MANUAL)
# Реализуем логику трех правильных ответов, либо одного неправильного.
    count = 0
    max_count = 3
    while count < max_count:
        argument, right_answer = game.meat()
        ans = answer(argument)
        if ans == right_answer:
            result = 'Correct'
            print(result)
            count += 1
        else:
            wrong_result = f"'{ans}' is wrong answer ;(."
            correct_result = f"Correct answer was '{right_answer}'"
            print(wrong_result, correct_result)
            return print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
