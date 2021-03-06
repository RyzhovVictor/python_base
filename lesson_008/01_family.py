# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    total_money = 0
    total_food = 0
    total_buy_coat = 0

    def __init__(self):
        self.count_money = 100
        self.count_food = 50
        self.count_mud = 0
        self.food_for_cat = 30

    def __str__(self):
        return 'В доме денег осталось: {}, кол-во еды осталось: {}, кол-во грязи осталось: {}'.format(self.count_money,
                                                                                                      self.count_food,
                                                                                                      self.count_mud)


class Man:
    def __init__(self, name):
        self.degree_satiety = 30
        self.degree_happy = 100
        self.house = home
        self.name = name

    def __str__(self):
        return 'Еды осталось: {}, уровень счастья: {}'.format(self.degree_satiety, self.degree_happy)

    def depression(self):
        if self.house.count_mud >= 90:
            self.degree_happy -= 5

    def food(self):
        self.degree_satiety -= 10

    def eat(self):
        if self.house.count_food >= 15:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.degree_satiety += 25
            self.house.total_food += 15
            self.house.count_food -= 15
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def petting_cat(self):
        self.degree_happy += 5
        cprint('{} погладил(а) кота'.format(self.name), color='yellow')

    def act(self):
        if (self.degree_satiety <= 0) or (self.degree_happy < 10):
            cprint('{} умер...'.format(self.name), color='red')
            return False
        self.depression()
        self.food()
        if self.degree_satiety <= 30:
            self.eat()
            return False
        return True


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    def __str__(self):
        return 'Я {}, Степень сытости: {} Степень счастья: {}'.format(self.name, self.degree_satiety,
                                                                      self.degree_happy)

    def act(self):

        if not super().act():
            return
        dice = randint(1, 5)
        if self.house.count_money <= 200:
            self.work()
        elif self.degree_happy < 30:
            self.gaming()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.work()
        elif dice == 4:
            self.work()
        elif dice == 5:
            self.petting_cat()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.count_money += 150
        self.house.total_money += 150

    def gaming(self):
        cprint('{} Играл в WoT'.format(self.name), color='green')
        self.degree_happy += 20


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    def __str__(self):
        return 'Я {}, Степень сытости: {} Степень счастья: {}'.format(self.name, self.degree_satiety,
                                                                      self.degree_happy)

    def act(self):
        if not super().act():
            return
        dice = randint(1, 5)
        if self.house.count_food <= 30:
            self.shopping()
        elif self.degree_happy < 30:
            self.buy_fur_coat()
        elif self.degree_happy <= 15:
            self.petting_cat()
        elif self.house.count_mud > 100:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.buy_fur_coat()
        elif dice == 5:
            self.petting_cat()

    def shopping(self):
        if self.house.count_money >= 150:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.count_money -= 150
            self.house.count_food += 150
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        if self.house.count_money >= 400:
            cprint('{} сходила в магазин за шубой'.format(self.name), color='magenta')
            self.house.count_money -= 350
            self.house.total_buy_coat += 350
            self.degree_happy += 60
        else:
            cprint('Денег на шубу нет!', color='red')

    def clean_house(self):
        if self.house.count_mud >= 100:
            self.house.count_mud -= 100
            cprint('{} Убралась'.format(self.name))


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = home
        self.degree_satiety = 30

    def __str__(self):
        return 'Я {}, Степень сытости: {}'.format(self.name, self.degree_satiety)

    def act(self):
        if self.degree_satiety <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.degree_satiety <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.tear_wallpaper()

    def eat(self):
        if self.house.count_food > 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.degree_satiety += 10
            self.house.total_food += 10
            self.house.count_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.degree_satiety -= 10
        cprint('{} спал весь день'.format(self.name), color='magenta')

    def tear_wallpaper(self):
        self.degree_satiety -= 10
        self.house.count_mud += 5
        cprint('{} драл обои целый день'.format(self.name), color='magenta')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self, name):
        self.name = name
        self.house = home
        self.degree_satiety = 30
        self.degree_happy = 100

    def __str__(self):
        return 'Я {}, Степень сытости: {} Степень счастья: {}'.format(self.name, self.degree_satiety,
                                                                      self.degree_happy)

    def act(self):
        if self.degree_satiety <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return
        dice = randint(1, 2)
        if self.degree_satiety <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()

    def eat(self):
        if self.house.count_food >= 15:
            cprint('{} поел(а)'.format(self.name), color='yellow')
            self.degree_satiety += 20
            self.house.total_food += 10
            self.house.count_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.degree_satiety -= 10
        cprint('{} спал весь день'.format(self.name), color='magenta')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')
    home.count_mud += 5

count_coat = int(home.total_buy_coat / 350)

cprint('Всего заработанных денег: {}'.format(home.total_money), color='yellow')
cprint('Всего съедено еды: {}'.format(home.total_food), color='yellow')
cprint('Всего купленно шуб: {}'.format(count_coat), color='yellow')

# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
murzik = Cat(name='Мурзик')
kolya = Child(name='Коля')

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murzik.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murzik, color='cyan')
    cprint(kolya, color='cyan')
    cprint(home, color='cyan')
    home.count_mud += 5

count_coat = int(home.total_buy_coat / 350)

cprint('Всего заработанных денег: {}'.format(home.total_money), color='yellow')
cprint('Всего съедено еды: {}'.format(home.total_food), color='yellow')
cprint('Всего купленно шуб: {}'.format(count_coat), color='yellow')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачёт!