#!/usr/bin/env python3
# Основной скрипт brain_games/scripts/brain_even.
# Проверка ответа на вопрос о четности в модулe brain_games/answer
# Подсчет с финальным ответом в модуле brain_games/count.py.
from brain_games.games import even
from brain_games.motor import skeleton


def main():
    skeleton(even)


if __name__ == '__main__':
    main()
