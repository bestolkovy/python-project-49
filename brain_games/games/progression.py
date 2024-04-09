# Логика для игры Арифметическая прогрессия
from random import randint


MANUAL = 'What number is missing in the progression?'


# Функция создания прогрессии
def make_progression():
    start = randint(2, 45)
    step = randint(2, 8)
    progression = [start + i * step for i in range(10)]
    return progression


# Функция создания строки из прогрессии со скрытым элементом.
def str_progression(progression):
    progression_str = progression.copy()
    hidden_num = randint(0, 9)
    progression_str[hidden_num] = '..'
    string_hidden_element = ' '.join(map(str, progression_str))
    return string_hidden_element, hidden_num


#  Создаем прогрессию, переводим в строку, вычисляем правильный ответ.
def meat():
    progression = make_progression()
    argument, hidden_num = str_progression(progression)
    right_answer = str(progression[hidden_num])
    return argument, right_answer
