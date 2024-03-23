from brain_games.brain_even.answer import answer


def count():
    k = answer()
    i = 0
    while k is True and i < 2:
        print("smart")
        i += 1
        k = answer()
    if k is False:
        print('dolboeb')
    else:
        print('MASTAR!!!')


