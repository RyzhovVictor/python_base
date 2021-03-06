# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snowflakes
from snowfall import draw_snowflakes
from snowfall import move_snowflakes
from snowfall import number_snowflakes
from snowfall import delete_snowflakes

sd.resolution = (1200, 600)

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль 05_snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

create_snowflakes(45)
color = sd.background_color
color_1 = sd.COLOR_YELLOW
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.start_drawing()
    draw_snowflakes(color)
    move_snowflakes()
    draw_snowflakes(color_1)
    fallen_flakes = number_snowflakes()
    if fallen_flakes:
        delete_snowflakes(number=fallen_flakes)
        create_snowflakes(45)
    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break


sd.pause()
#зачёт!