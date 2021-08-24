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
    def __init__(self, input_file, output_file, group):
        self.input_file = input_file
        self.output_file = output_file
        self.group = group
        self.stat = {}

    def read_minute(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            for line in file:
                if 'NOK' in line:
                    line = line.strip()[1:self.group]
                    if line in self.stat:
                        self.stat[line] += 1
                    else:
                        self.stat[line] = 1

    def write(self):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            for dates, count in self.stat.items():
                file.write(f'[{dates}] {count}\n')


class Events_hours(Events):
    def read_hours(self):
        self.read_minute()


class Events_month(Events):
    def read_month(self):
        self.read_minute()


class Events_years(Events):
    def read_years(self):
        self.read_minute()


processing_minute = Events('events.txt', 'sort_minute.txt', 17)
processing_minute.read_minute()
processing_hours = Events_hours('events.txt', 'sort_hours.txt', 14)
processing_hours.read_hours()
processing_month = Events_month('events.txt', 'sort_month.txt', 8)
processing_month.read_month()
processing_years = Events_years('events.txt', 'sort_years.txt', 5)
processing_years.read_years()


processing_minute.write()
processing_hours.write()
processing_month.write()
processing_years.write()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
