# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(300, 300)


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
# TODO все def надо держать в верхенй части программы, а остальной код после всех def

# TODO Вместо дублирования векторов надо написать цикл
# цикл по диапазону углов (0, 360, шаг_угла)
#     вектор(точка, переменная цикла...)
#     точка = концу_вектора
# TODO Такой цикл позволит сильно сократить код.
# TODO Помимо этого расширит возможности, позволяя рисовать множество разных многоугольников

def triangle(point, angle=0, length=200):
    t1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    t1.draw()

    t2 = sd.get_vector(start_point=t1.end_point, angle=angle + 120, length=length, width=3)
    t2.draw()

    t3 = sd.get_vector(start_point=t2.end_point, angle=angle + 240, length=length, width=3)
    t3.draw()
# TODO Если приблизить итоговую фигуру, нарисованную векторами, будет заметен разрыв между последней стороной
# TODO и начальной точкой.
# TODO Этот разрыв надо убрать.
# TODO Происходит это потому, что вектор рисуется из одной точки, а координаты второй рассчитываются
# TODO Расчёты округляются до целых чисел (тк нельзя нарисовать пол пикселя)
# TODO Из-за этого появляются неточности, которые копятся с каждой стороной и в итоге происходит разрыв.
# TODO В нашем случае решить это можно с помощью sd.line() вместо последнего вектора.

point_0 = sd.get_point(100, 200)
length = 200

triangle(point=point_0, angle=0, length=length)

point_square = sd.get_point(350, 350)


def square(point_square, angle=0, length=200):
    s1 = sd.get_vector(start_point=point_square, angle=angle, length=length, width=3)
    s1.draw()

    s2 = sd.get_vector(start_point=s1.end_point, angle=angle + 90, length=length, width=3)
    s2.draw()

    s3 = sd.get_vector(start_point=s2.end_point, angle=angle + 180, length=length, width=3)
    s3.draw()

    s4 = sd.get_vector(start_point=s3.end_point, angle=angle - 90, length=length, width=3)
    s4.draw()


length = 200
point_1 = sd.get_point(400, 200)

square(point_square=point_1, angle=0, length=length)

point_pentagon = sd.get_point(300, 300)


def pentagon(point_pentagon, angle=0, length=100):
    p1 = sd.get_vector(start_point=point_pentagon, angle=angle, length=length, width=3)
    p1.draw()

    p2 = sd.get_vector(start_point=p1.end_point, angle=angle + 72, length=length, width=3)
    p2.draw()

    p3 = sd.get_vector(start_point=p2.end_point, angle=angle + 144, length=length, width=3)
    p3.draw()

    p4 = sd.get_vector(start_point=p3.end_point, angle=angle + 216, length=length, width=3)
    p4.draw()

    p5 = sd.get_vector(start_point=p4.end_point, angle=angle + 288, length=length, width=3)
    p5.draw()


length = 100
point_2 = sd.get_point(700, 200)

pentagon(point_pentagon=point_2, angle=0, length=length)

point_hexagon = sd.get_point(100, 550)


def hexagon(point_hexagon, angle=0, length=100):
    h1 = sd.get_vector(start_point=point_hexagon, angle=angle, length=length, width=3)
    h1.draw()

    h2 = sd.get_vector(start_point=h1.end_point, angle=angle + 60, length=length, width=3)
    h2.draw()

    h3 = sd.get_vector(start_point=h2.end_point, angle=angle + 120, length=length, width=3)
    h3.draw()

    h4 = sd.get_vector(start_point=h3.end_point, angle=angle + 180, length=length, width=3)
    h4.draw()

    h5 = sd.get_vector(start_point=h4.end_point, angle=angle + 240, length=length, width=3)
    h5.draw()

    h6 = sd.get_vector(start_point=h5.end_point, angle=angle + 300, length=length, width=3)
    h6.draw()


length = 100
point_3 = sd.get_point(1000, 200)

hexagon(point_hexagon=point_3, angle=0, length=length)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
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
