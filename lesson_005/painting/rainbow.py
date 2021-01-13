import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1200, 600)

point = sd.get_point(600, -150)
radius = 600
for rainbow in rainbow_colors:
    radius += 5
    sd.circle(center_position=point, radius=radius, color=rainbow, width=4)

sd.pause()