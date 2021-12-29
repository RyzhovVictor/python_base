# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_elements(figure_point, length_tri, angle_tri):
        angle = (n - 2) / n * 180
        new_angle = 0 + angle_tri
        point1 = figure_point
        for _ in range(0, n - 1):
            v1 = sd.get_vector(figure_point, new_angle, length_tri, 2)
            v1.draw()
            new_angle += 180 - angle
            figure_point = v1.end_point
        sd.line(point1, figure_point, width=2)
    return draw_elements


draw_triangle = get_polygon(n=3)
draw_triangle(figure_point=sd.get_point(100, 200), length_tri=100, angle_tri=0)

draw_square = get_polygon(n=4)
draw_square(figure_point=sd.get_point(350, 200), length_tri=100, angle_tri=0)

draw_pentagon = get_polygon(n=5)
draw_pentagon(figure_point=sd.get_point(650, 200), length_tri=100, angle_tri=0)

draw_hexagon = get_polygon(n=6)
draw_hexagon(figure_point=sd.get_point(950, 200), length_tri=100, angle_tri=0)

sd.pause()
#зачёт!