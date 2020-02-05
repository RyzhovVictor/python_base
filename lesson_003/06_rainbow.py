# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1200, 600)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_point = sd.get_point(50, 50)
end_point = sd.get_point(350, 450)


def rainbow(line, step):
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_BLACK, width=4)
    line += step


for x in range(100, 701, 100):
    start_point = sd.get_point(x, 50)
    end_point = sd.get_point(x, 450)
    rainbow(line=100, step=5)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
