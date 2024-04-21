# движок для всех игр
from brain_games.cli import welcome_user
import prompt


def play_game(game=None):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    count = 0
    ROUND_COUNT = 3
    if not game:
        return
    print(game.MANUAL)
    while count < ROUND_COUNT:
        argument, right_answer = game.get_question_and_answer()
        print(f'Question: {argument}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            result = 'Correct'
            print(result)
            count += 1
        else:
            wrong_result = f"'{answer}' is wrong answer ;(."
            correct_result = f"Correct answer was '{right_answer}'"
            print(wrong_result, correct_result)
            return print(f"Let's try again, {name}!")
    return print(f'Congratulations, {name}!')
