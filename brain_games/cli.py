import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def answer(quest):
    print(f'Question: {quest}')
    answ = prompt.string('Your answer: ')
    return answ
