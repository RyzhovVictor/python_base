import simple_draw as sd

sd.resolution = [1800, 800]


def sun():
    sd.circle(sd.get_point(50, 750), radius=50, color=sd.COLOR_YELLOW, width=0)
    for angle in range(0, 360, 24):
        sd.vector(sd.get_point(50, 750), angle, 100, sd.COLOR_YELLOW, 10)


