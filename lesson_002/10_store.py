#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

tables_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']

table_code = goods['Стол']
tables_item = store[table_code][0]
tables_quantity = tables_item['quantity']
tables_price = tables_item['price']
tables_cost = tables_quantity * tables_price

tables_cost_1 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']

table_code = goods['Стол']
tables_item = store[table_code][1]
tables_quantity_1 = tables_item['quantity']
tables_price_1 = tables_item['price']

total_tables_cost = (tables_price * tables_quantity) + (tables_price_1 * tables_quantity_1)
total_tables_quantity = tables_quantity + tables_quantity_1

print('Стол -', total_tables_quantity, 'шт, стоимость', total_tables_cost, 'руб')

sofa_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']

sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_quantity = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost = sofa_quantity * sofa_price

sofa_cost_1 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']

sofa_code = goods['Диван']
sofa_item = store[sofa_code][1]
sofa_quantity_1 = sofa_item['quantity']
sofa_price_1 = sofa_item['price']

total_sofa_cost = (sofa_price * sofa_quantity) + (sofa_price_1 * sofa_quantity_1)
total_sofa_quantity = sofa_quantity + sofa_quantity_1

print('Диван -', total_sofa_quantity, 'шт, стоимость', total_sofa_cost, 'руб')

chairs_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']

chair_code = goods['Стул']
chairs_item = store[chair_code][0]
chairs_quantity = chairs_item['quantity']
chairs_price = chairs_item['price']
chairs_cost = chairs_quantity * chairs_price

chairs_cost_1 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']

chair_code = goods['Стул']
chairs_item = store[chair_code][1]
chairs_quantity_1 = chairs_item['quantity']
chairs_price_1 = chairs_item['price']

chairs_cost_2 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']

chair_code = goods['Стул']
chairs_item = store[chair_code][2]
chairs_quantity_2 = chairs_item['quantity']
chairs_price_2 = chairs_item['price']

total_chairs_cost = (chairs_price * chairs_quantity) + (chairs_price_1 * chairs_quantity_1) + (
        chairs_price_2 * chairs_quantity_2)
total_chairs_quantity = chairs_quantity + chairs_quantity_1 + chairs_quantity_2

print('Стул -', total_chairs_quantity, 'шт, стоимость', total_chairs_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################

#зачет!