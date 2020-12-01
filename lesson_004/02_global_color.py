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
    # TODO названия надо распечатывать из словаря, циклом
    # TODO чтобы была связь между тем, что выводится на экран и тем, что печатается
    # TODO тогда мы сможем добавлять цвет в словарь и это автоматически отразится в печати
    for input_users in colors:
        print('Выбирете желаемый цвет для фигур:\n1 : красный \n2 : оранжевый \n3 : желтый \n4 : зеленый \n5 : '
              'сине-зеленый \n6 : синий \n7 : фиолетовый\n')

        input_users = input('Введите желаемй цвет: ')  # TODO название лучше подобрать другое, user_input например
        # TODO а то у вас в коде очень много переменных с таким названием
        while True:
            # TODO попробуйте тут реализовать запрос нового ввода в цикле while до тех пор
            # TODO пока число не окажется правильным
            if input_users in colors:
                user_input = colors[input_users]  # TODO формат тут не нужен
                print(colors[user_input][
                          'sd_name'])  # TODO сейчас вы передаете {'color_name': 'yellow', 'sd_name': (255, 255, 0)}
                # TODO colors[ввод_пользователя]['sd_name'] -- нужно добавить такой ключ
                return input_users
            else:
                print('Вы ввели не корректный номер:')
                continue


# TODO Что-то я больше запутался. Не могу разобраться.


draw_elements()

sd.pause()
