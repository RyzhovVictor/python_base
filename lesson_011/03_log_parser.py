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
        # TODO изначально создайте old min = None
        while True:
            try:
                line = next(gen)
                if 'NOK' in line:
                    # TODO Вот тут, внутри, проверьте - old min is None?
                    # TODO если да, то запишите в неё текущую линию
                    line = line[1:self.group]
                    old_min = line[1:self.group]  # TODO это действие надо
                    # будет убрать (внутрь проверки)
                    if line and old_min in self.stat:
                        # TODO проверка некорректная, Line не будет проверен
                        #  внутри self.stat
                        # TODO Да и в целом old min не нужно в проверки
                        #  добавлять
                        self.stat[line] += 1
                    else:
                        old_min = self.stat[line]  # TODO это действие
                        # выполнять не нужно
                        self.stat[line] = 1
                        yield old_min, self.stat[old_min]
                        old_min = line
                    # print(self.stat[line])
                    # print(line)
                    # print(old_line)
                    # TODO так вы будете возвращать текущую минуту и всегда с единичкой
                    # TODO а надо вернуть прошлую
            except StopIteration:
                # print(self.stat)
                return


# TODO т.е. вся цепочка идет так
# TODO текущие минуты считаем --> находим новую минуту --> отправляем старую минуту yield-ом --> обновляем старую минуту на текущую --> считаем текущую и повторяем всё
# TODO в конце, когда строки кончились - после цикла выполняем возврат того, что осталось в line и stat[line]


file_name = "events.txt"
parse = Events(file_name)

grouped_events = parse.run()

for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
