import simple_draw as sd

sd.resolution = (1800, 800)

brick_x, brick_y = 100, 50


def wall():
    sd.rectangle(left_bottom=sd.get_point(450, 0), right_top=sd.get_point(1050, 400), color=sd.COLOR_RED,
                 width=0)
    sd.rectangle(left_bottom=sd.get_point(450, 0), right_top=sd.get_point(1050, 400), color=sd.COLOR_BLACK,
                 width=3)


def brick_wall():
    step = 0
    for row, y in enumerate(range(0, 400, brick_y)):
        y1 = y + 50
        if row % 2 == 0:
            step = 450
        else:
            step = 500
        for x in range(step, 1000, 100):
            x1 = x + 100
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x1, y1)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_BLACK, width=3)


def roof():
    sd.polygon(point_list=[sd.get_point(300, 400), sd.get_point(1200, 400), sd.get_point(750, 600)],
               color=sd.COLOR_DARK_ORANGE, width=0)
    sd.polygon(point_list=[sd.get_point(300, 400), sd.get_point(1200, 400), sd.get_point(750, 600)],
               color=sd.COLOR_BLACK, width=3)


def window():
    sd.rectangle(left_bottom=sd.get_point(550, 50), right_top=sd.get_point(850, 300), color=sd.COLOR_WHITE,
                 width=0)
    sd.rectangle(left_bottom=sd.get_point(550, 50), right_top=sd.get_point(850, 300), color=sd.COLOR_DARK_ORANGE,
                 width=7)



def window_frame():
    sd.line(start_point=sd.get_point(700, 300), end_point=sd.get_point(700, 50), color=sd.COLOR_DARK_ORANGE, width=10)
    sd.line(start_point=sd.get_point(550, 175), end_point=sd.get_point(850, 175), color=sd.COLOR_DARK_ORANGE, width=10)




