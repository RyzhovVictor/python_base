# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class Events:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.stat = {}

    def read(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            for line in file:
                if 'NOK' in line:
                    line = line.strip()[1:17]
                    if line in self.stat:
                        self.stat[line] += 1
                    else:
                        self.stat[line] = 1

    def write(self):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            for dates, count in self.stat.items():
                # print(f'[{dates}] {count}')
                file.write(f'[{dates}] {count}\n')


processing = Events('events.txt', 'output_file.txt')
processing.read()
processing.write()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
