# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
    if input_data > str(len(input_data[4])):
        raise BaseException('Вы ввели больше 5 значений')
except ValueError:
    print('Нужно писать цифры')
except IndexError:
    print('Нужно ввести 5 цифр')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
