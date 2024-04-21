# Логика для игры Арифметическая прогрессия
from random import randint


MANUAL = 'What number is missing in the progression?'


# Функция создания прогрессии
def make_progression(initial_term, common_diff, NUM_OF_TERMS):
    progression = [initial_term + i * common_diff for i in range(NUM_OF_TERMS)]
    return progression


# Функция создания строки из прогрессии со скрытым элементом.
def str_progression(progression, hidden_num):
    progression_str = progression.copy()
    progression_str[hidden_num] = '..'
    string_hidden_element = ' '.join(map(str, progression_str))
    return string_hidden_element


#  Создаем прогрессию, переводим в строку, вычисляем правильный ответ.
def get_question_and_answer():
    MIN_INITIAL_TERM = 2
    MAX_INITIAL_TERM = 45
    MIN_COMMON_DIFF = 2
    MAX_COMMON_DIFF = 8
    MIN_HIDDEN_INDEX = 0
    NUM_OF_TERMS = 20
    initial_term = randint(MIN_INITIAL_TERM, MAX_INITIAL_TERM)
    common_diff = randint(MIN_COMMON_DIFF, MAX_COMMON_DIFF)
    hidden_index = randint(MIN_HIDDEN_INDEX, NUM_OF_TERMS - 1)
    progression = make_progression(initial_term, common_diff, NUM_OF_TERMS)
    argument = str_progression(progression, hidden_index)
    right_answer = str(progression[hidden_index])
    return argument, right_answer
