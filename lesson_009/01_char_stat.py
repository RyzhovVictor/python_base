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

    def printed(self):
        txt = '+'
        print(f'+{txt:-^30}+')

        txt = '|'  # TODO выделять под одиночные символы переменную на одну операцию - не стоит
        # TODO лучше сократить код и просто вставить эти символы в строку напрямую
        # TODO (либо сформировать атрибут-словарь например и там все их расположить, но это надо хорошо обдумать)
        txt_1 = 'Буква'
        txt_2 = 'Частота'
        print(f'|{txt_1:^13} {txt:^1} {txt_2:^14}|')

        txt = '+'
        print(f'+{txt:-^30}+')

        total_count = 0
        # TODO сортировку надо выносить в отдельный метод
        # TODO представьте, что методы - это ваши работники
        # TODO вы платите каждому за свою работу
        # TODO но тут внезапно человек, который занимался печатью документов внезапно должен ещё заниматься сортировкой
        # TODO разве это будет правильно?
        # TODO (такой принцип в целом хорошо влияет на программу, т.к. каждая сущность (метод в нашем случае)
        # TODO будет отвечать за одно небольшое дело, тогда мы сможем быстро вычислять проблему, если они возникнут
        # TODO либо сможем быстро изменять код, если будет такая необходимость)
        for alphabet, count in sorted(self.stat.items(), key=self.sort_for_table, reverse=False):
            txt = '|'
            print(f'|{alphabet:^13} {txt:^1} {count:^14}|')
            total_count += count

        txt = '+'
        print(f'+{txt:-^30}+')

        txt = '|'
        txt_1 = 'ИТОГО'
        txt_2 = total_count
        print(f'|{txt_1:^13} {txt:^1} {txt_2:^14}|')
        txt = '+'
        print(f'+{txt:-^30}+')


statletter = StatLetter(file_name='voyna-i-mir.txt.zip')
statletter.collect()
statletter.printed()
# TODO во второй части можно будет создать наследников от класса выше
# TODO и переопределить только метод сортировки.
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
