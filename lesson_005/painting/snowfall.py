import simple_draw as sd

sd.resolution = (1200, 600)


def snowfall(N):
    snowflake = []
    for _ in range(N):
        snowflake.append(([sd.random_number(50, 1250), sd.random_number(550, 1600), sd.random_number(23, 47)]))

        for snow in snowflake:
            x, y, length = snow
            point = sd.get_point(x, y)

            sd.snowflake(center=point, length=length, color=sd.background_color, factor_a=0.6)
            if y > 10:
                snow[1] = sd.random_number(-30, 50)
                snow[0] = sd.random_number(-30, 1850)
                point_fall = sd.get_point(x, y)
                sd.snowflake(point_fall, length=length, color=sd.COLOR_WHITE)
            else:
                last_point = sd.get_point(x, y - 1)
                sd.snowflake(last_point, length, color=sd.COLOR_WHITE)
                snow[1] = sd.random_number(10, 30)
                break
        # sd.sleep(0.1)
        if sd.user_want_exit():
            break
        # sd.clear_screen()











