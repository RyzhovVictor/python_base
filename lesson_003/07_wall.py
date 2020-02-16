# -*- coding: utf-8 -*-

# (цикл for)
import row as row
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1200, 600)

step = 0
for y in range(0, 600, 50):
    y1 = y + 50
    step -= 50
    for x in range(step, 1200, 100):
        x1 = x + 100
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_RED, width=3)

sd.pause()
