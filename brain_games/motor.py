# движок для всех игр
from brain_games.cli import welcome_user
from brain_games.answer import answer
from brain_games.scripts.brain_games import main


def skeleton(game):
    main()
    name = welcome_user()
    print(game.MANUAL)
    count = 0
    while count < 3:
        argument, right_answer = game.meat()
        ans = answer(argument)
        if ans == right_answer:
            print("Correct!")
            count += 1
        else:
            return print(f"'{ans}' is wrong answer ;(. Correct answer was '{right_answer}'. \n Let's try again, {name}")
    return print(f'Congratulations, {name}!')
