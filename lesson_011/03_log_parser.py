# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

class Events:
    def __init__(self, input_file):
        self.input_file = input_file
        self.group = 17
        self.stat = {}

    def read_minute(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            yield from file

    def run(self):
        gen = self.read_minute()
        while True:
            try:
                line = next(gen)
                if 'NOK' in line:
                    line = line[1:self.group]
                    if line in self.stat:
                        self.stat[line] += 1
                        yield self.stat[line], line  # TODO yield нужно делать только тогда, когда находится новая минута
                    else:
                        self.stat[line] = 1
                        # TODO т.е. вот тут, в else надо выполнять yield + один yield после цикла, чтобы вернуть последнюю запись
            except StopIteration:
                break


file_name = "events.txt"
parse = Events(file_name)

grouped_events = parse.run()

for group_time, event_count in grouped_events:
    print(f'[{event_count}] {group_time}')
