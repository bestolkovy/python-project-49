# движок для всех игр
from brain_games.cli import welcome_user
from brain_games.answer import answer
# from brain_games.scripts.brain_games import main


def skeleton(game=''):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if game == '':
        return 'huy'
    print(game.MANUAL)
    count = 0
    max_count = 3
    while count < max_count:
        argument, r_a = game.meat()
        ans = answer(argument)
        if ans == r_a:
            result = 'Correct'
            print(result)
            count += 1
        else:
            result = f"'{ans}' is wrong answer ;(. Correct answer was '{r_a}'"
            print(result)
            return print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
