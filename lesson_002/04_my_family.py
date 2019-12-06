#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother' 'father' 'sister']

# список списков приблизителного роста членов вашей семьи
my_family_height = {
    'mother': (167),
    'father': (174),
    'sister': (158),
}

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

height_father = (174)

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

mother = my_family_height['mother']
father = my_family_height['father']
sister = my_family_height['sister']

total_height = (mother + father + sister)

print('father_height:', height_father, 'cm')
print('total_height:', total_height, 'cm')
