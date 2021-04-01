# -*- coding: utf-8 -*-
import simple_draw as sd
import random

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = random.choice([x_value for x_value in range(-25, 1225)])
        self.y = random.choice([y_value for y_value in range(700, 1400)])
        self.size_ray = random.choice([size_value for size_value in range(10, 50, 2)])
        self.color = sd.COLOR_WHITE

    def draw(self, color):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.size_ray, color=color)

    def move(self):
        self.y -= 25
        delta = random.randint(-5, 5)
        self.x += delta

    def can_fall(self):
        return self.y <= self.size_ray


flake = Snowflake()


def get_flakes(n=3):
    # от глобальных операторов надо отказываться
    # ими стоит пользоваться только в редких случаях
    # в данном задании можно обойтись без них
    snowflakes = []
    for i in range(0, n):
        # n создается где-то снаружи - это плохая практика
        # т.к. функция становится зависима от этой переменной и её где-то надо искать
        # чтобы изменить количество снежинок
        # передавайте это число параметром
        snowflakes.append(Snowflake())
    return snowflakes


flakes = get_flakes()


def get_fallen_flakes(snowflakes):
    global num_fallen
    num_fallen = []
    for num in enumerate(flakes):
        print(num)
        if flake.can_fall():  # TODO К какой flake применяется can_fall?
            snowflakes.append(num)  # TODO num - это что? как проверить?
    print(num_fallen)
    return num_fallen


def append_flakes():
    for index in enumerate(flakes):
        print(index)
        flakes.append(index)
        return flakes  # TODO return - это конец функции
    # TODO выполнив return пайтон завершает функцию на этом месте и дальше продолжает выполнять уже другой код
    # TODO в этом случае ваш цикл добавит один индекс в flakes и завершит функцию вместе с циклом
    # TODO вы такую логику задумывали для этого кода?
    # TODO + непонятно, что и зачем вы добавляете в список flakes?
    # TODO добавил принт, чтобы это можно было проверить


def remove_flakes(number):
    for i in number[::-1]:
        del flakes[i]


# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

while True:
    sd.start_drawing()
    for flake in flakes:
        flake.draw(sd.background_color)
        flake.move()
        flake.draw(sd.COLOR_WHITE)
    fallen_flakes = get_fallen_flakes(get_flakes())
    # TODO get_flakes() - что сделает при вызове?
    # TODO как проверить - проверяете ли вы начальный список снежинок или нет?
    # TODO попробуйте
    # TODO 1) уменьшить количество снежинок, чтобы было попроще проверку делать
    # TODO 2) в начало get_fallen_flakes добавьте print(snowflakes)
    # TODO вы увидите, что передается совершенно новый список снежинок, а старый список не проверяется
    if fallen_flakes:
        print('+')  # TODO добавил ещё один принт, чтобыы проверить - срабатывает ли это условие
        append_flakes()
        flake.draw(sd.background_color)
        remove_flakes(fallen_flakes)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
