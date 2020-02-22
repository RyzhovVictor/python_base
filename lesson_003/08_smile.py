# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd

sd.resolution = (1200, 600)

sd.background_color = [0, 255, 255]


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(coordinate_x, coordinate_y, color):
    point = sd.get_point(coordinate_x, coordinate_y)
    sd.circle(center_position=point, radius=100, color=sd.COLOR_YELLOW, width=0)
    point = sd.get_point(coordinate_x, coordinate_y)
    sd.circle(center_position=point, radius=100, color=sd.COLOR_BLACK, width=2)
    point = sd.get_point(coordinate_x - 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=15, color=color, width=5)
    point = sd.get_point(coordinate_x + 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=15, color=color, width=5)
    point = sd.get_point(coordinate_x - 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=12, color=sd.COLOR_WHITE, width=0)
    point = sd.get_point(coordinate_x + 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=12, color=sd.COLOR_WHITE, width=0)
    point = sd.get_point(coordinate_x + 35, coordinate_y + 35)
    sd.snowflake(center=point, length=7, color=sd.COLOR_RED, factor_a=0.35, factor_b=1.4, factor_c=50)
    point = sd.get_point(coordinate_x - 35, coordinate_y + 35)
    sd.snowflake(center=point, length=7, color=sd.COLOR_RED, factor_a=0.35, factor_b=1.4, factor_c=50)
    point = sd.get_point(coordinate_x + 40, coordinate_y + 35)
    sd.circle(center_position=point, radius=10, color=sd.COLOR_BLACK, width=0)
    point = sd.get_point(coordinate_x - 31, coordinate_y + 35)
    sd.circle(center_position=point, radius=10, color=sd.COLOR_BLACK, width=0)
    point = [sd.get_point(coordinate_x + -5, coordinate_y + 32), sd.get_point(coordinate_x - 25, coordinate_y - 15),
             sd.get_point(coordinate_x + 2, coordinate_y - 15)]
    sd.lines(point_list=point, color=color, closed=False, width=3)
    point = [sd.get_point(coordinate_x + -2, coordinate_y - 55), sd.get_point(coordinate_x - + 35, coordinate_y - 50)]
    sd.lines(point_list=point, color=color, closed=False, width=3)


color = [0, 0, 0]
smile(600, 300, color)

for _ in range(10):
    point_random = sd.random_number(0, 1200)
    smile(point_random, point_random, color)

sd.pause()
# Красота! :)))
#зачет!