# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snowflakes
from snowfall import draw_snowflakes
from snowfall import move_snowflakes
from snowfall import number_snowflakes
from snowfall import delete_snowflakes
from snowfall import flakes


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

create_snowflakes(20)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.start_drawing()
    for flake in flakes:  # TODO здесь не нужен цикл по снежинкам
        # TODO в draw_snowflakes и других функциях уже зашиты свои циклы
        # TODO тут нужно просто вызывать эти функции в правильном порядке
        draw_snowflakes(sd.background_color)
        move_snowflakes()
        draw_snowflakes(sd.COLOR_YELLOW)
        draw_snowflakes(sd.background_color)
        fallen_flakes = number_snowflakes()
        delete_snowflakes(number=fallen_flakes)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():  # TODO дублирование кода надо убрать
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
