# Логика для игры Арифметическая прогрессия
from random import randint


MANUAL = 'What number is missing in the progression?'


# Функция создания прогрессии
def make_progression(start, step):
    progression = [start + i * step for i in range(10)]
    return progression


# Функция создания строки из прогрессии со скрытым элементом.
def str_progression(progression, hidden_num):
    progression_str = progression.copy()
    progression_str[hidden_num] = '..'
    string_hidden_element = ' '.join(map(str, progression_str))
    return string_hidden_element


#  Создаем прогрессию, переводим в строку, вычисляем правильный ответ.
def meat():
    start = randint(2, 45)
    step = randint(2, 8)
    hidden_num = randint(0, 9)
    progression = make_progression(start, step)
    argument = str_progression(progression, hidden_num)
    right_answer = str(progression[hidden_num])
    return argument, right_answer
