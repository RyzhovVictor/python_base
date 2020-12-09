# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# N = 20


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

def snowfall(N):
    snowflake = []
    for _ in range(N):
        snowflake.append(([sd.random_number(-50, 1250), sd.random_number(550, 1600), sd.random_number(23, 47)]))

    # TODO цикл while должен начинаться после цикла for, а не внутри него
        while True:
            sd.start_drawing()
            # TODO start - в начале, перед циклом for
            # TODO finish - в конце, перед sd.sleep
            # TODO Сами по себе эти функции нужны, чтобы не рисовать каждое промежуточное действие по-отдельности
            # TODO start останавливает рисование, finish запускает рисование всего, что накопилось с момента start-а
            for snow in snowflake:
                x, y, length = snow
                point = sd.get_point(x, y)

                sd.snowflake(center=point, length=length, color=sd.background_color, factor_a=0.6)
                if y > 50:
                    snow[1] -= 10
                    x -= sd.random_number(-25, 25)  # TODO это изменение тоже надо производить по индексу
                    # TODO snow[0] -= ...
                    # TODO иначе оно не будет сохранено в списке, т.к изменяться будет только переменная x
                    point_fall = sd.get_point(x, y)
                    sd.snowflake(point_fall, length=length, color=sd.COLOR_WHITE)
                else:
                    last_point = sd.get_point(x, y - 1)
                    sd.snowflake(last_point, length, color=sd.COLOR_WHITE)
                    y += sd.random_number(600, 800)  # TODO и тут, snow[1] +=

            sd.finish_drawing()
            sd.sleep(0.01)
            if sd.user_want_exit():
                break
            # sd.clear_screen()


snowfall(20)

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
