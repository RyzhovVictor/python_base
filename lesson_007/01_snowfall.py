# -*- coding: utf-8 -*-
import simple_draw as sd
import random

sd.resolution = (1200, 600)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
n = 20


class Snowflake:
    def __init__(self):
        self.x = random.choice([x_value for x_value in range(50, 1150, 50)])
        self.y = random.choice([y_value for y_value in range(800, 1900, 55)])
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
        if self.y <= self.size_ray:
            # TODO В данном случае if/else блок лишний, можно оставить просто return с условием
            # TODO Т.к. само по себе условие равно либо True, либо False
            # TODO пример return a > b
            return True


flake = Snowflake()


def get_flakes():
    snowflakes = []
    for i in range(0, n):
        snowflakes.append(Snowflake())
    return snowflakes


flakes = get_flakes()


def get_fallen_flakes(snowflakes):
    # num_fallen = []
    # TODO создавать список для индексов - хорошая идея
    for num in range(0, len(flakes)):  # TODO от range+len надо уходить https://habr.com/ru/company/ruvds/blog/485648/
        if flake.can_fall():
            snowflakes.append(num)
    # TODO в итоге вы должны пустой список заполнить индексами и вернуть список индексов упавших снежинок
    # TODO тут можно принт добавить чтобы проверить, что всё возвращается верно
    return snowflakes


def append_flakes(fallen_flakes):
    # TODO range + len стоит убрать
    for i in range(0, len(fallen_flakes)):
        if flake.can_fall():  # TODO тут эта проверка не нужна. + какая именно снежинка проверяется в ней?
            flakes.append(Snowflake())


def remove_flakes(fallen_flakes, snowflakes):
    # TODO range + len замените на проход по развернотому списку (индекс[::-1])
    for i in range(len(fallen_flakes) - 1, -1, -1):
        if i in fallen_flakes:  # TODO проверка не нужна
            del snowflakes[i]


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
        if not flake.can_fall():  # TODO эта проверка не нужна (либо ей можно встроить внутрь move
            flake.move()
        flake.draw(sd.COLOR_WHITE)
    fallen_flakes = get_fallen_flakes(snowflakes=[])  # TODO пустой список стоит создавать внутри самой функцции
    if fallen_flakes:
        append_flakes(fallen_flakes)
        flake.draw(sd.background_color)
        remove_flakes(fallen_flakes, snowflakes=flakes)

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
