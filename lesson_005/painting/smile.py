import simple_draw as sd

# sd.resolution = (1200, 600)


# sd.background_color = [0, 255, 255]


def smile(coordinate_x, coordinate_y, color):
    point = sd.get_point(coordinate_x, coordinate_y)
    sd.circle(center_position=point, radius=100, color=sd.COLOR_YELLOW, width=0)
    point = sd.get_point(coordinate_x, coordinate_y)
    sd.circle(center_position=point, radius=100, color=sd.COLOR_BLACK, width=2)
    point = sd.get_point(coordinate_x - 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=15, color=color, width=5)
    point = sd.get_point(coordinate_x + 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=15, color=color, width=5)
    point = sd.get_point(coordinate_x - 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=12, color=sd.COLOR_WHITE, width=0)
    point = sd.get_point(coordinate_x + 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=12, color=sd.COLOR_WHITE, width=0)
    point = sd.get_point(coordinate_x + 35, coordinate_y + 35)
    sd.circle(center_position=point, radius=10, color=sd.COLOR_BLACK, width=0)
    point = sd.get_point(coordinate_x - 31, coordinate_y + 35)
    sd.circle(center_position=point, radius=10, color=sd.COLOR_BLACK, width=0)
    point = [sd.get_point(coordinate_x + -5, coordinate_y + 32), sd.get_point(coordinate_x - 25, coordinate_y - 15),
             sd.get_point(coordinate_x + 2, coordinate_y - 15)]
    sd.lines(point_list=point, color=color, closed=False, width=3)
    point = [sd.get_point(coordinate_x + -2, coordinate_y - 55), sd.get_point(coordinate_x - + 35, coordinate_y - 50)]
    sd.lines(point_list=point, color=color, closed=False, width=3)


color = [0, 0, 0]
smile(600, 300, color)

sd.pause()
