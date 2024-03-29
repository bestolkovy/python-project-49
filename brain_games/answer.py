import prompt


def answer(quest):
    print(f'Question: {quest}')
    answ = prompt.string('Your answer: ')
    return answ
