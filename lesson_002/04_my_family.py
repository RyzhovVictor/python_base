#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Лида' + 'Вася' + 'Соня']

# список списков приблизителного роста членов вашей семьи
my_family_height = [['Лида', 167], ['Вася', 174], ['Соня', 158]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

height_father = my_family_height[1][1]

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

lida = my_family_height[0][1]
vasya = my_family_height[1][1]
sonya = my_family_height[2][1]

total_height = (lida + vasya + sonya)

print('father_height:', height_father, 'cm')
print('total_height:', total_height, 'cm')
