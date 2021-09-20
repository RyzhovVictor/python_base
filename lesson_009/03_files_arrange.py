# -*- coding: utf-8 -*-

import os
import datetime
import shutil
import time

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


folder = []
file_open = r'E:\Users\Desktop\Vito\Python\python_base\icons'
path_sorted_files = r'E:\Users\Desktop\Vito\Python\python_base\icons_by_year'


def create_date(address, file):
    create_time = os.path.getmtime(address + '/' + file)
    print_datetime = datetime.datetime.fromtimestamp(create_time)
    print(f'|{address}\{file} {"":-^15}{">"} {print_datetime}|')
    return datetime.datetime.fromtimestamp(create_time)


def create_month():
    for path in range(1, 13):
        if path > 9:
            if not os.path.exists(str(path)):
                os.makedirs(str(path))
        else:
            if not os.path.exists('0' + str(path)):
                os.makedirs('0' + str(path))


def create_years():
    for address, dirs, files in os.walk(file_open):
        for file in files:
            if file[-3:] not in folder:
                folder.append(file[-3:])
            if file[-3:] in folder:
                year = str(create_date(address, file))[:10][:4]
                os.chdir(path_sorted_files)
                if not os.path.exists(year):
                    os.makedirs(year)
                os.chdir(path_sorted_files + os.sep + year)
                create_month()


def move_files():
    for address, dirs, files in os.walk(file_open):
        for file in files:
            if file[-3:] in folder:
                year = str(create_date(address, file))[:10][:4]
                month = str(create_date(address, file))[:10][5:7]
                shutil.copy2(address + os.sep + file,
                             path_sorted_files + os.sep + year + os.sep + month + os.sep + file)
            else:
                print('Перенос не выполнен')


create_years()
move_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
