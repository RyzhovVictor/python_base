# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


# Элементы сложения: Вода, Воздух, Огонь, Земля.
# Элементы результата: Шторм, Пар, Грязь, Молния, Пыль, Лава.

class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(element_1=self, element_2=other)
        elif isinstance(other, Fire):
            return Steam(element_1=self, element_2=other)
        elif isinstance(other, Earth):
            return Mud(element_1=self, element_2=other)
        if isinstance(other, Wood):
            return Raft(element_1=self, element_2=other)


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(element_1=self, element_2=other)
        elif isinstance(other, Fire):
            return Lighting(element_1=self, element_2=other)
        elif isinstance(other, Earth):
            return Dust(element_1=self, element_2=other)
        elif isinstance(other, Wood):
            return FlyingLeaves(element_1=self, element_2=other)


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam(element_1=self, element_2=other)
        elif isinstance(other, Air):
            return Lighting(element_1=self, element_2=other)
        elif isinstance(other, Earth):
            return Lava(element_1=self, element_2=other)
        elif isinstance(other, Wood):
            return Bonfire(element_1=self, element_2=other)


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud(element_1=self, element_2=other)
        elif isinstance(other, Air):
            return Dust(element_1=self, element_2=other)
        elif isinstance(other, Fire):
            return Lava(element_1=self, element_2=other)
        elif isinstance(other, Wood):
            return House(element_1=self, element_2=other)


class Wood:
    def __str__(self):
        return 'Дерево'

    def __add__(self, other):
        if isinstance(other, Water):
            return Raft(element_1=self, element_2=other)
        elif isinstance(other, Air):
            return FlyingLeaves(element_1=self, element_2=other)
        elif isinstance(other, Fire):
            return Bonfire(element_1=self, element_2=other)
        elif isinstance(other, Earth):
            return House(element_1=self, element_2=other)


class Storm:
    def __str__(self):
        return 'Шторм'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class Steam:
    def __str__(self):
        return 'Пар'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class Mud:
    def __str__(self):
        return 'Грязь'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class Lighting:
    def __str__(self):
        return 'Молния'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class Dust:
    def __str__(self):
        return 'Пыль'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class Lava:
    def __str__(self):
        return 'Лава'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class Raft:
    def __str__(self):
        return 'Плот'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class Bonfire:
    def __str__(self):
        return 'Костер'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class House:
    def __str__(self):
        return 'Дом'

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


class FlyingLeaves:
    def __str__(self):
        return 'Летящие листья '

    def __init__(self, element_1, element_2):
        self.element_1 = element_1
        self.element_2 = element_2


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Wood(), '+', Fire(), '=', Wood() + Fire())
print(Wood(), '+', Earth(), '=', Wood() + Earth())
print(Air(), '+', Wood(), '=', Air() + Wood())
print(Water(), '+', Wood(), '=', Water() + Wood())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

#зачёт!