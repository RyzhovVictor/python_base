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


class Carma:
    ENLIGHTENMENT_CARMA_LEVEL = 777
    count = 0

    def get_target_karma(self):
        return self.ENLIGHTENMENT_CARMA_LEVEL

    def get_karma(self):
        return self.count

    def set_karma(self, point):
        self.count += point

    def reach_enlightenment(self):
        if self.get_karma() >= self.get_target_karma():
            return True


def one_day(life):
    sin_num = random.randint(1, 10)
    sins = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']

    try:
        if sin_num == 10:
            raise BaseException
    except BaseException:
        exception = random.choice(sins)
        return exception
    else:
        life.set_karma(random.randint(1, 7))


human = Carma()
days_passed = 0
parse_sins = []

while True:
    if human.reach_enlightenment():
        print(f'|{"+":*^35}|')
        print(f'| {"": ^} Карма накопилась через {days_passed} дней {" ": ^1}|')
        print(f'|{"+":*^35}|')
        break
    else:
        x = one_day(human)
        days_passed += 1
        if x is not None:
            parse_sins.append(x)

print('Запись исключений в лог:')
print('\n'.join(parse_sins))

# https://goo.gl/JnsDqu
#зачёт!