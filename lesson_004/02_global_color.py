# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def all_in(point, angle, length, count, color):
    v2 = sd.get_vector(point, angle, length)
    step = (360 // count) - 1
    for cur_angle in range(step):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=color)
        point = v1.end_point
        angle += count
    sd.line(start_point=point, end_point=v2.start_point, width=3, color=color)


def triangle(point, angle, length, color):
    step = 120
    all_in(point, angle, length, step, color)


def square(point, angle, length, color):
    step = 90
    all_in(point, angle, length, step, color)


def pentagon(point, angle, length, color):
    step = 72
    all_in(point, angle, length, step, color)


def hexagon(point, angle, length, color):
    step = 60
    all_in(point, angle, length, step, color)


t_point = sd.get_point(100, 200)
s_point = sd.get_point(350, 200)
p_point = sd.get_point(650, 200)
h_point = sd.get_point(950, 200)


def draw_elements():
    color = user_input()
    # TODO тут можно проверить, работает ли правильно функция
    print('Из функции user_input мы получили значение -', color)
    # TODO сейчас этот принт выводит - "Из функции user_input мы получили значение - None"
    triangle(t_point, 0, 100, color)
    square(s_point, 0, 100, color)
    pentagon(p_point, 0, 100, color)
    hexagon(h_point, 0, 100, color)


colors = {
    '1': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
    '2': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
    '3': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
    '4': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
    '5': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
    '6': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
    '7': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}
}


# TODO Названия цветов и значения цветов - 2 связанных элемента, которые необходимы нам для
# TODO работы этого алгоритма.
# TODO Поэтому в этом случае удобнее создать словарь следующей структуры
# TODO словарь = {'0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},...}
# TODO Таким образом для каждого цвета у нас будет свой словарь. И у каждого словаря будут одинаковые ключи
# TODO 'color_name' и 'sd_name'
# TODO Тогда можно будет легко проверить ввод (user_input in словарь)
# TODO А если среди ключей есть выбор пользователя - по этому ключу мы получим нужный вложенный словарь
# TODO А там все ключи одинаковые, можем получить как название цвета, так и sd_цвет


def user_input():
    print('*' * 10, 'НАЧАЛО', '*' * 10, )
    for number, color in colors.items():
        # TODO в этом цикле надо распечатать элементы словаря, что-то подобное вы уже делали в 03.05
        # TODO только тут структура попроще. Используйте метод items() на словаре
        # TODO распечатайте переменную цикла, потом подумайте - как с её помощью распечатать именно названия цветов
        # print('Выбирете желаемый цвет для фигур:\n1 : красный \n2 : оранжевый \n3 : желтый \n4 : зеленый \n5 : '
        #       'сине-зеленый \n6 : синий \n7 : фиолетовый\n')
        # TODO Тут попробуйте распечатать input_users
        print(number, '-', color['color_name'])
        # TODO Подумайте, как можно взять отсюда только номера и названия цветов
    print('*' * 10, 'КОНЕЦ', '*' * 10, )

    # TODO код ниже не нужно помещать внутрь цикла for, этот код должен выполнять после цикла for, а не вместе с ним
    # TODO т.е. должен быть отступ как у этой тудушки

    input_users = input('Введите желаемй цвет: ')
    while True:
        if input_users in colors:
            user_input = (colors[input_users]['sd_name'], t_point)
            return
            # здесь нужно выполнить return выбранного цвета
            # TODO return - это указатель на то, что нужно вернуть, если он остаётся пустым, как у вас
        # TODO то он ничего не вернет, надо писать что именно возвращать - return ввод_пользователя например
        else:
            print('Вы ввели не корректный номер:')

    # TODO сам вбор цвета записан правильно, работать это будет
    # TODO хотя можно это и упростить, если перенести условие проверки input_users in colors
    # TODO в условие цикла while (while input_users not in colors)
    # TODO тогда от проверки внутри помжно будет отказаться (но это пока необзяательно, сперва разберемся с тем,
    # TODO что уже готово)


# TODO первые пометки вроде исправил, но проблема вылета ошибки осталась

draw_elements()

sd.pause()
