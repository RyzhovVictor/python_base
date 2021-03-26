import simple_draw as sd
import random

sd.resolution = (1200, 600)


def create_snowflakes(n):
    global snowflakes
    snowflakes = []
    for i in range(0, n):
        snowflakes.append(([sd.random_number(-50, 1250), sd.random_number(550, 1600), sd.random_number(23, 47)]))
    return snowflakes


def draw_snowflakes(color):
    x = snowflakes[0]
    y = snowflakes[1]
    point = sd.get_point(x, y)
    size_ray = snowflakes[2]
    color = sd.COLOR_WHITE
    sd.snowflake(center=point, length=size_ray, color=color)


def move_snowflakes():
    snowflakes[1] -= 25
    delta = random.randint(-5, 5)
    snowflakes[0] += delta


flakes = create_snowflakes(20)


def number_snowflakes():
    new_snowflakes = []
    for num in range(0, len(flakes)):
        if snowflakes[1] <= snowflakes[2]:
            new_snowflakes.append(num)
    return snowflakes


def delete_snowflakes(number):
    for i in range(len(number) - 1, -1, -1):
        if i in number:
            del snowflakes[i]


sd.pause()
