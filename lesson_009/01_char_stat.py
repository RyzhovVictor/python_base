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

    def sort_10_1(self):
        self.sorted_date = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)

    def printed(self):
        print(f'+{"+":-^30}+')
        print(f'|{"Буква":^13} {"|":^1} {"Частота":^14}|')
        print(f'+{"+":-^30}+')
        for alphabet, count in self.sorted_date:
            print(f'|{alphabet:^13} {"|":^1} {count:^14}|')
            self.total_count += count
        print(f'+{"+":-^30}+')
        print(f'|{"ИТОГО":^13} {"|":^1} {self.total_count:^14}|')
        print(f'+{"+":-^30}+')

    def run(self):
        self.collect()
        self.sort_10_1()
        self.printed()


class Sorting(StatLetter):
    # TODO идея в том, чтобы конкретную сортировку переопределить для текущео класса
    # TODO (т.е. 1 класс = 1 сортировка)
    def sort_1_10(self):
        self.sorted_date = sorted(self.stat.items(), key=lambda x: x[1], reverse=False)

    def sort_Z_A(self):
        self.sorted_date = sorted(self.stat.items(), key=lambda x: x[0], reverse=True)

    def sort_A_Z(self):
        self.sorted_date = sorted(self.stat.items(), key=lambda x: x[0], reverse=False)

    def run(self):  # TODO метод run переопределять не нужно, он должен вызывать всё ту же сортировку
        # TODO которую вызывает родитель (используйте какое-то общее название для сортировок, чтобы не путаться)
        self.collect()
        self.sort_1_10()
        self.printed()
        self.collect()
        self.sort_Z_A()
        self.printed()
        self.collect()
        self.sort_A_Z()
        self.printed()


stat_letter = StatLetter(file_name='voyna-i-mir.txt.zip')
stat_letter.run()

sorting = Sorting(file_name='voyna-i-mir.txt.zip')
sorting.run()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
