import simple_draw as sd

sd.resolution = (1200, 600)


def snowfall(n):
    # TODO здесь вы собрали все действия, как это было в 4 модуле
    # TODO но тут мы как раз хотим уйти от проблем, которые были в том модуле
    # TODO и сделать код, который будет готов к масштабированию
    # TODO (так мы учимся правилам разделения кода, которые пригодятся при работе над реальным проектами)
    # TODO В условиях перечислены функции, которые тут должны быть
    # сделать модуль 05_snowfall.py в котором реализовать следующие функции
    #  создать_снежинки(N) - создает N снежинок
    #  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
    #  сдвинуть_снежинки() - сдвигает снежинки на один шаг
    #  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
    #  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
    # снежинки хранить в глобальных переменных модуля snowfall
    # TODO Каждая функция выполняет свою отдельную задачу независимо от других
    # TODO Это позволяет в дальнейшем выбирать часть кода и переписывать её не меняя при этом остальные
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

#  Я вроде бы создал первую функцию создание снежинок N штук, что здесь не так ?

def snowflake_color(color):
    pass


# Не понимаю как из этой функции перенести значения первой функции с измененными данными в виде цвета

snowflake_color(sd.COLOR_RED)
sd.pause()
