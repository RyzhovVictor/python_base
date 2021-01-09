# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from pprint import pprint
from district.central_street.house1.room1 import folks as central_street_h1_r1
from district.central_street.house1.room2 import folks as central_street_h1_r2
from district.central_street.house2.room1 import folks as central_street_h2_r1
from district.central_street.house2.room2 import folks as central_street_h2_r2
from district.soviet_street.house1.room1 import folks as soviet_street_h1_r1
from district.soviet_street.house1.room2 import folks as soviet_street_h1_r2
from district.soviet_street.house2.room1 import folks as soviet_street_h2_r1
from district.soviet_street.house2.room2 import folks as soviet_street_h2_r2

residents = [', '.join(central_street_h1_r1), ', '.join(central_street_h1_r2), ', '.join(central_street_h2_r1),
             ', '.join(central_street_h2_r2), ', '.join(soviet_street_h1_r1), ', '.join(soviet_street_h1_r2),
             ', '.join(soviet_street_h2_r1), ', '.join(soviet_street_h2_r2)]

pprint("На районе живут: " + ', '.join(map(str, residents)))
