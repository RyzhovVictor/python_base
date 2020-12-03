# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.resolution = (1200, 600)


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


# t_point = sd.get_point(100, 200)
# s_point = sd.get_point(350, 200)
# p_point = sd.get_point(650, 200)
# h_point = sd.get_point(950, 200)


colors = {
    '1': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
    '2': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
    '3': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
    '4': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
    '5': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
    '6': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
    '7': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}
}

figures = {
    '1': {'figure_name': 'triangle', 'point': sd.get_point(600, 300)},
    '2': {'figure_name': 'square', 'point': sd.get_point(600, 300)},
    '3': {'figure_name': 'pentagon', 'point': sd.get_point(600, 300)},
    '4': {'figure_name': 'hexagon', 'point': sd.get_point(600, 300)},
}


def draw_elements():
    color = user_input()
    type_figures = user_input_type_figures()
    triangle(type_figures, 0, 100, color)
    square(type_figures, 0, 100, color)
    pentagon(type_figures, 0, 100, color)
    hexagon(type_figures, 0, 100, color)


def user_input():
    print('*' * 10, 'НАЧАЛО', '*' * 10, )
    for number, color in colors.items():
        print(number, '-', color['color_name'])
    print('*' * 10, 'КОНЕЦ', '*' * 10, )
    while True:
        input_users = input('Введите желаемй цвет: ')
        if input_users in colors:
            user_input_1 = colors[input_users]['sd_name']
            return user_input_1
        else:
            print('Вы ввели не корректный номер:')


def user_input_type_figures():
    print('*' * 10, 'НАЧАЛО', '*' * 10, )
    for number, type_figures in figures.items():
        print(number, '-', type_figures['figure_name'])
    print('*' * 10, 'КОНЕЦ', '*' * 10, )
    while True:
        input_users_1 = input('Введите желаемую фигуру: ')
        if input_users_1 in figures:
            user_input_2 = figures[input_users_1]['point']
            return user_input_2
        else:
            print('Вы ввели не корректный номер:')


draw_elements()

sd.pause()
