import simple_draw as sd

sd.resolution = (1200, 600)


def snowfall(n):
    snowflake = []
    for _ in range(n):
        snowflake.append(([sd.random_number(0, 1200), sd.random_number(550, 1600), sd.random_number(23, 47)]))

    while True:
        sd.start_drawing()
        for snow in snowflake:
            x, y, length = snow
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE, factor_a=0.6)

            if y > 50:
                snow[1] -= 10
                point_fall = sd.get_point(x, y)
                sd.snowflake(point_fall, length=length, color=sd.COLOR_WHITE)
            else:
                last_point = sd.get_point(x, y - 1)
                sd.snowflake(last_point, length, color=sd.COLOR_WHITE)
                snow[1] += 1250

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
        sd.clear_screen()


snowfall(20)


def snowflake_color(color):
    pass


# Не понимаю как из этой функции перенести значения первой функции с измененными данными в виде цвета

snowflake_color(sd.COLOR_RED)
sd.pause()
