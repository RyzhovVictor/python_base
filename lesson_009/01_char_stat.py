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

    # def sort_for_frequency(self, pair):  # TODO эти два метода можно убрать
    #     return pair[1]
    #
    # def sort_for_letters(self, pair):
    #     return pair[0]

    def sort(self):
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

    # TODO Добавьте метод run
    # TODO в котором будут вызываться по очереди нужные методы collect + sort + printed

    # TODO не совсем то, что подразумевается под шаблонным методом
    # TODO идея вот какая - в родителе мы реализуем один тип работы
    # TODO при этом изменяемую часть в этой работе надо выделить в отдельный метод с минимумом кода
    # TODO в наследниках мы переопределяем только этот отдельный метод
    # TODO и в итоге получаем программу, которая работает иначе
    # TODO Здесь эта часть - сортировка
    # TODO можно написать
    # TODO деф сортировка(селф):
    # TODO     селф.сортированные_данные = сортед(...)
    # TODO и всё, одной строчки хватит
    # TODO дальше создаем наследника и в нём пишем этот же метод
    # TODO деф сортировка(селф):
    # TODO     селф.сортированные_данные = сортед(..., reverse=True)  -- но изменяем тип сортировки
    # TODO ВСЕ остальные методы наследник возьмёт у родителя, но сортировка будет новой
    # TODO из-за этого работать наследник будет иначе.
    # TODO Чтобы реализовать эту идею вам нужно:
    # TODO 1) Выделить сортировку в отдельный метод (у вас сейчас она совмещена с печатью)
    # TODO 2) вернуть печать ОДНОГО типа данных в родителя (без дублирования под каждую сортировку)
    # TODO 3) создать наследников с изменением ОДНОГО метода из ОДНОЙ строчки


class Sorting(StatLetter):
    def sort(self):
        self.sorted_date = sorted(self.stat.items(), key=self.sort_for_frequency, reverse=False)
        # TODO здесь напрямую укажите вместо self.sort_for_frequency
        # TODO lambda x: x[0]

    def printed(self):  # TODO здесь printed можно убрать
        print(f'+{"+":-^30}+')
        print(f'|{"Буква":^13} {"|":^1} {"Частота":^14}|')
        print(f'+{"+":-^30}+')
        self.sort()
        print(f'+{"+":-^30}+')
        print(f'|{"ИТОГО":^13} {"|":^1} {self.total_count:^14}|')
        print(f'+{"+":-^30}+')


sorting = Sorting(file_name='voyna-i-mir.txt.zip')
sorting.collect()
sorting.printed()

stat_letter = StatLetter(file_name='voyna-i-mir.txt.zip')
stat_letter.collect()
stat_letter.printed()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
