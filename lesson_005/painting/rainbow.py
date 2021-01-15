import simple_draw as sd

sd.resolution = (1800, 800)


def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    point = sd.get_point(600, -200)
    radius = 1200
    for rainbow_style in rainbow_colors:
        radius += 25
        sd.circle(center_position=point, radius=radius, color=rainbow_style, width=25)

