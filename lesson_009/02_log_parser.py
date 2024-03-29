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
        self.group = 17
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


class EventsHours(Events):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)
        self.group = 14


class EventsMonth(Events):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)
        self.group = 8


class EventsYears(Events):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)
        self.group = 5


processing_minute = Events('events.txt', 'sort_minute.txt')
processing_minute.read_minute()
processing_minute.write()
processing_hours = EventsHours('events.txt', 'sort_hours.txt')
processing_hours.read_minute()
processing_hours.write()
processing_month = EventsMonth('events.txt', 'sort_month.txt')
processing_month.read_minute()
processing_month.write()
processing_years = EventsYears('events.txt', 'sort_years.txt')
processing_years.read_minute()
processing_years.write()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
#зачёт!