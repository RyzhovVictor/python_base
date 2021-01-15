import simple_draw as sd

sd.resolution = (1200, 800)

point_0 = sd.get_point(600, 50)


def draw_branches(point, angle, length):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_DARK_GREEN)
    next_point = v1.end_point
    next_angle = angle - (sd.random_number(20, 40))
    next_length = length * (sd.random_number(60, 80) / 100)
    next_angle_1 = angle + (sd.random_number(30, 50))
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    draw_branches(point=next_point, angle=next_angle_1, length=next_length)




