# Основной скрипт brain_games/scripts/brain_even.
# Проверка ответа на вопрос о четности в модулe brain_games/answer
# Подсчет с финальным ответом в модуле brain_games/count.py.
from brain_games.brain_even.answer import answer
import brain_games.cli
import brain_games.scripts.brain_games

# Объявление игры. Приветствие с запросом имени игрока
brain_games.scripts.brain_games.main()
name = brain_games.cli.welcome_user()


# Функция подсчета правильных ответов.
def count():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        k = answer()
        if k is False:
            print(f"Let's try again, {name}")
            break
    if i == 2:
        print(f'Congratulations, {name}!')
