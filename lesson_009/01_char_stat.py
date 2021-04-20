# -*- coding: utf-8 -*-

import zipfile
from random import randint

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

file_name = 'voyna-i-mir.txt'
stat = {}

with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        for prev_char in line:
            if prev_char.isalpha():
                if prev_char in stat:
                    stat[prev_char] += 1
                else:
                    stat[prev_char] = 1

txt = '+'
print(f'+{txt:-^30}+')

txt = '|'
txt_1 = 'Буква'
txt_2 = 'Частота'
print(f'|{txt_1:^13} {txt:^1} {txt_2:^14}|')

txt = '+'
print(f'+{txt:-^30}+')

total_count = 0
for alphabet, count in stat.items():
    txt = '|'
    print(f'|{alphabet:^13} {txt:^1} {count:^14}|')
    total_count += count
    # for sort in sorted(str(count)):
    #     txt = '|'
    #     print(f'|{alphabet:^13} {txt:^1} {count:^14}|')
    #     total_count += count

txt = '+'
print(f'+{txt:-^30}+')

txt = '|'
txt_1 = 'ИТОГО'
txt_2 = total_count
print(f'|{txt_1:^13} {txt:^1} {txt_2:^14}|')
txt = '+'
print(f'+{txt:-^30}+')


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
