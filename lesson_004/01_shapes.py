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


def all_in(point, angle=0, length=200):
    # TODO 1) angle - параметр сразу же перезаписывается angle из цикла
    # TODO (и то, и то - создает переменную с одним название)
    start_angle = 0
    angle = start_angle + 120
    point = sd.get_point(200, 450)
    for angle in range(0, 360):  # TODO Переменной нужно было задать только шаг (0, 360 - шаг, шаг)
        # TODO При этом старайтесь не использовать кучу одинаковых названий

        # TODO в этой функции надо использовать не конкретный угол
        # TODO нужна переменная, которая этот угол будет изменять при необходимости

        # TODO нужно задать правильный диапазон, чтобы лишних итераций просто не было
        t1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        # TODO У вас будет 2 угла (начальный - переданный параметром, и угол из переменной цикла,
        # TODO нужно использовать и тот, и другой)

        # TODO а в векторе нужно использовать и параметр и переменную цикла
        # TODO angle = start_angle + angle
        t1.draw()
        point = t1.end_point
    t2 = sd.line(start_point=point, end_point=sd.get_point(100, 200), width=3)
    # TODO тут вы используете конкретную точку - делать так не стоит
    # TODO Линия должна соединять первую точку, которую передали сюда
    # TODO и последнюю точку, на которой остановился последний вектор.
    # TODO 1ую точку надо до цикла сохранить в отдельную переменную
    # TODO 2ую точку (point которая изменялась в цикле) вы задаете правильно


point = sd.get_point(200, 450)

all_in(point, 0, 200)
sd.pause()

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
