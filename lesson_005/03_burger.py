# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from my_burger import bun
from my_burger import chops
from my_burger import cucumber
from my_burger import tomato
from my_burger import mayonnaise
from my_burger import cheese

double_cheeseburger = [bun(), chops(), cucumber(), tomato(), mayonnaise(), cheese()]

print('Рецепт двойного чизбургера: ', double_cheeseburger)
#зачёт!