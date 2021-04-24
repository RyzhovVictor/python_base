# -*- coding: utf-8 -*-

import zipfile


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

class StatLetter:
    def __init__(self, file_name):
        self.total_count = 0
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        global filename
        z_file = zipfile.ZipFile(self.file_name, 'r')
        for filename in z_file.namelist():
            z_file.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for prev_char in line:
            if prev_char.isalpha():
                if prev_char in self.stat:
                    self.stat[prev_char] += 1
                else:
                    self.stat[prev_char] = 1

    def sort_for_table(self, pair):
        return pair[1]

    def decreasing_frequency(self):
        for alphabet, count in sorted(self.stat.items(), key=self.sort_for_table, reverse=True):
            print(f'|{alphabet:^13} {"|":^1} {count:^14}|')
            self.total_count += count

    def printed(self):
        print(f'+{"+":-^30}+')
        print(f'|{"Буква":^13} {"|":^1} {"Частота":^14}|')
        print(f'+{"+":-^30}+')
        self.decreasing_frequency()
        print(f'+{"+":-^30}+')
        print(f'|{"ИТОГО":^13} {"|":^1} {self.total_count:^14}|')
        print(f'+{"+":-^30}+')


class Sorting(StatLetter):
    def increasing_frequency(self):
        for alphabet, count in sorted(self.stat.items(), key=self.sort_for_table, reverse=False):
            print(f'|{alphabet:^13} {"|":^1} {count:^14}|')
            self.total_count += count

    def descending_letters(self):
        for alphabet, count in sorted(self.stat.items(), key=self.sort_for_table, reverse=False):
            print(f'|{alphabet:^13} {"|":^1} {count:^14}|')
            self.total_count += count

    def printed(self):
        print(f'+{"+":-^30}+')
        print(f'|{"Буква":^13} {"|":^1} {"Частота":^14}|')
        print(f'+{"+":-^30}+')
        self.increasing_frequency()
        print(f'+{"+":-^30}+')
        print(f'|{"ИТОГО":^13} {"|":^1} {self.total_count:^14}|')
        print(f'+{"+":-^30}+')

        print(f'+{"+":-^30}+')
        print(f'|{"Буква":^13} {"|":^1} {"Частота":^14}|')
        print(f'+{"+":-^30}+')
        self.descending_letters()
        print(f'+{"+":-^30}+')
        print(f'|{"ИТОГО":^13} {"|":^1} {self.total_count:^14}|')
        print(f'+{"+":-^30}+')




stat_letter = StatLetter(file_name='voyna-i-mir.txt.zip')
stat_letter.collect()
stat_letter.printed()

sorting = Sorting(file_name='voyna-i-mir.txt.zip')
sorting.collect()
sorting.printed()
# TODO во второй части можно будет создать наследников от класса выше
# TODO и переопределить только метод сортировки.
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
