import simple_draw as sd

sd.resolution = (1200, 600)


def create_snowflakes(n):
    global snowflakes
    snowflakes = []
    for i in range(0, n):
        snowflakes.append(([sd.random_number(-50, 1400), sd.random_number(700, 1600), sd.random_number(23, 47)]))
    return snowflakes


def draw_snowflakes(color):
    for snow in snowflakes:
        x, y, size_ray = snow
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=size_ray, color=color)


def move_snowflakes():
    for coordinate in snowflakes:
        if coordinate[1] > 50:
            coordinate[1] -= 20
            coordinate[0] -= 4
            point_fall = sd.get_point(coordinate[0], coordinate[1])
            sd.snowflake(point_fall, length=coordinate[2], color=sd.COLOR_WHITE)
        else:
            last_point = sd.get_point(coordinate[0], coordinate[1] - 1)
            sd.snowflake(last_point, coordinate[2], color=sd.COLOR_WHITE)
            coordinate[1] += 1250


def number_snowflakes():
    global new_snowflakes
    new_snowflakes = []
    for index, flake in enumerate(snowflakes):
        if snowflakes[1] <= snowflakes[2]:
            new_snowflakes.append(index)
    return new_snowflakes


def delete_snowflakes(number):
    for i in number[::-1]:
        del new_snowflakes[i]
