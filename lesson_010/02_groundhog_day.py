# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random

ENLIGHTENMENT_CARMA_LEVEL = 777


def printed():
    print(f'+{"+":-^50}+')


excep = []


def one_day():
    file_log = f'| Сегодня я '
    dice = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    carma = random.randint(1, 7)
    if carma == random.choice(dice):
        raise Exception('IamGodError')
    printed()
    print(f'{file_log}{exc.args}{"|":^47}')
    printed()
    excep.append(exc.args)
    if carma == random.choice(dice):
        try:
            raise BaseException('DrunkError')
        except BaseException as exc:
            printed()
            print(f'{file_log}{exc.args}{"|":^49}')
            printed()
            excep.append(exc.args)
    if carma == random.choice(dice):
        try:
            raise BaseException('CarCrashError')
        except BaseException as exc:
            printed()
            print(f'{file_log}{exc.args}{"|":^44}')
            printed()
            excep.append(exc.args)
    if carma == random.choice(dice):
        try:
            raise BaseException('GluttonyError')
        except BaseException as exc:
            printed()
            print(f'{file_log}{exc.args}{"|":^44}')
            printed()
            excep.append(exc.args)
    if carma == random.choice(dice):
        try:
            raise BaseException('DepressionError')
        except BaseException as exc:
            printed()
            print(f'{file_log}{exc.args}{"|":^40}')
            printed()
            excep.append(exc.args)
    if carma == random.choice(dice):
        try:
            raise BaseException('SuicideError')
        except BaseException as exc:
            printed()
            print(f'{file_log}{exc.args}{"|":^45}')
            printed()
            excep.append(exc.args)
    return carma


total_carma = 0


def parse_log():
    count = 0
    print(f'{"|":*<79}|')
    print(f'{"|":<79}|')
    print(f'|{"":>30}{"PARSE LOG EXCEPTION"}{"":<29}|')
    print(f'{"|":<79}|')
    print(f'{"|":*<79}|')
    for line in excep:
        count += 1
        print(f'{"-":->80}')
        print(f'Исключения {">":->15} {line}, {">":->15} счетчик - {count}')
        print(f'{"-":->80}')


while True:  # TODO вместо True здесь можно условие выхода из цикла прописать
    print(f'{total_carma} - Ух! Карма растет!')
    if total_carma <= ENLIGHTENMENT_CARMA_LEVEL:
        # TODO вот здесь можно добавить try/except
        total_carma += one_day()
    else:
        break

parse_log()

# https://goo.gl/JnsDqu
