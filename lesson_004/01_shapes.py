# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

#
# def triangle(point, angle=0, length=200):
#     for angle in range(0, 360, 120):
#         if angle < 240:
#             t1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#             t1.draw()
#             point = t1.end_point
#     t2 = sd.line(start_point=point, end_point=sd.get_point(100, 200), width=3)
#
#
# point_square = sd.get_point(350, 350)
#
#
# def square(point_square, angle=0, length=200):
#     for angle in range(0, 360, 90):
#         if angle < 270:
#             s1 = sd.get_vector(start_point=point_square, angle=angle, length=length, width=3)
#             s1.draw()
#             point_square = s1.end_point
#     s2 = sd.line(start_point=point_square, end_point=sd.get_point(400, 200), width=3)
#
#
# point_pentagon = sd.get_point(300, 300)
#
#
# def pentagon(point_pentagon, angle=0, length=100):
#     for angle in range(0, 360, 72):
#         if angle < 288:
#             p1 = sd.get_vector(start_point=point_pentagon, angle=angle, length=length, width=3)
#             p1.draw()
#             point_pentagon = p1.end_point
#     p2 = sd.line(start_point=point_pentagon, end_point=sd.get_point(700, 200), width=3)
#
#
# point_hexagon = sd.get_point(100, 550)
#
#
# def hexagon(point_hexagon, angle=0, length=100):
#     for angle in range(0, 360, 60):
#         if angle < 300:
#             h1 = sd.get_vector(start_point=point_hexagon, angle=angle, length=length, width=3)
#             h1.draw()
#             point_hexagon = h1.end_point
#     h2 = sd.line(start_point=point_hexagon, end_point=sd.get_point(1000, 200), width=3)
#
#
# point_0 = sd.get_point(100, 200)
# length = 200
#
# triangle(point=point_0, angle=0, length=length)
#
# length = 200
# point_1 = sd.get_point(400, 200)
#
# square(point_square=point_1, angle=0, length=length)
#
# length = 100
# point_2 = sd.get_point(700, 200)
#
# pentagon(point_pentagon=point_2, angle=0, length=length)
#
# length = 100
# point_3 = sd.get_point(1000, 200)
#
# hexagon(point_hexagon=point_3, angle=0, length=length)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.


def all_in(point, angle, length, count):
    v2 = sd.get_vector(point, angle, length)
    step = (360 // count) - 1
    for cur_angle in range(step):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        point = v1.end_point
        angle += count
    sd.line(start_point=point, end_point=v2.start_point, width=3)


def triangle(point, angle, length):
    step = 120
    all_in(point, angle, length, step)


def square(point, angle, length):
    step = 90
    all_in(point, angle, length, step)


def pentagon(point, angle, length):
    step = 72
    all_in(point, angle, length, step)


def hexagon(point, angle, length):
    step = 60
    all_in(point, angle, length, step)


t_point = sd.get_point(100, 200)
s_point = sd.get_point(350, 200)
p_point = sd.get_point(650, 200)
h_point = sd.get_point(950, 200)

triangle(t_point, 0, 100)
square(s_point, 0, 100)
pentagon(p_point, 0, 100)
hexagon(h_point, 0, 100)

# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
#зачёт!