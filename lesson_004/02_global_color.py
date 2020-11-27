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

# TODO Не могли бы еще раз проверить это задание, вроде выполненно.

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
    triangle(t_point, 0, 100, color)
    square(s_point, 0, 100, color)
    pentagon(p_point, 0, 100, color)
    hexagon(h_point, 0, 100, color)


colors = {
    '1': sd.COLOR_RED,
    '2': sd.COLOR_ORANGE,
    '3': sd.COLOR_YELLOW,
    '4': sd.COLOR_GREEN,
    '5': sd.COLOR_CYAN,
    '6': sd.COLOR_BLUE,
    '7': sd.COLOR_PURPLE
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
    print('Выбирете желаемый цвет для фигур:\n1 : красный \n2 : оранжевый \n3 : желтый \n4 : зеленый \n5 : '
          'сине-зеленый \n6 : синий \n7 : фиолетовый\n')
    color = input('Введите желаемй цвет: ')
    # TODO попробуйте тут реализовать запрос нового ввода в цикле while до тех пор
    # TODO пока число не окажется правильным
    if color in colors:
        color = colors['{0}'.format(color)]
        return color
    else:
        print('Вы ввели не корректный номер:')


draw_elements()

sd.pause()
