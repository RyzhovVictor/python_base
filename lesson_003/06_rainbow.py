# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1200, 600)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

start_point = sd.get_point(50, 50)
end_point = sd.get_point(350, 450)
for colors in rainbow_colors:
    sd.line(start_point, end_point, color=colors, width=4)
# TODO Точки зависят от координат, а координаты - это просто числа.
# TODO Изменяете координаты (x + 5 например)--> создаете точку заново (get_point(...)) --> используете эту точку
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(600, -150)
radius = 600
for rainbow in rainbow_colors:
    radius += 5
    sd.circle(center_position=point, radius=radius, color=rainbow, width=4)

sd.pause()
