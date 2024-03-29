import prompt
#from brain_games.brain_even.arg import argument, zadanie, right_answer
#from brain_games.brain_even.arg import name1


# Вывод случайного числа и ответ игрока четное оно или нет. Проверка ответа.
def answer(list, name):
    print(f'Question: {list[0]}')
    answ = prompt.string('Your answer: ')
    if answ == list[1]:
        print("Correct!")
        return True
    else:
        print(f"'{answ}' is wrong answer ;(. Correct answer was '{list[1]}'.")
        print(f"Let's try again, {name}")
        return False
 

def count(name, argument, right_answer):
    ans = answer(argument, right_answer)
    for i in range(3):
        if ans is False:
            print(f"Let's try again, {name}")
            break
        else:
            ans = answer(argument, right_answer)
        if i == 2 and ans is True:
            print(f'Congratulations, {name}!')


def test_del():
    for i in range(3):
        answer(right_answer())
