# -*- coding: utf-8 -*-

import os
import datetime
import shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class SortedFiles:

    def __init__(self):
        self.folder = []
        self.parent_dir = os.path.dirname(os.path.abspath(r'lesson_009'))
        self.file_open = (self.parent_dir + os.sep + r'icons')
        self.path_sorted_files = (self.parent_dir + os.sep + r'icons_by_year')

    def create_date(self, address, file):
        create_time = os.path.getmtime(address + os.sep + file)
        print_datetime = datetime.datetime.fromtimestamp(create_time)
        print(f'|{address}{os.sep}{file} {"":-^15}{">"} {print_datetime}|')
        return datetime.datetime.fromtimestamp(create_time)

    def move_files(self):
        for address, dirs, files in os.walk(self.file_open):
            for file in files:
                if file not in self.folder:
                    self.folder.append(file)
                    year = str(self.create_date(address, file))[:10][:4]
                    month = str(self.create_date(address, file))[:10][5:7]
                    os.makedirs(self.path_sorted_files + os.sep + year + os.sep + month, exist_ok=True)
                    shutil.copy2(address + os.sep + file,
                                 self.path_sorted_files + os.sep + year + os.sep + month + os.sep + file)
                else:
                    print('Перенос не выполнен')

    def run(self):
        self.move_files()


sorted_files = SortedFiles()
sorted_files.run()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
