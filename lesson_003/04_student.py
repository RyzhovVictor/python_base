# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
expenses -= educational_grant
total_expenses = expenses
i = 0
while i < 9:
    i += 1
    total_expenses *= 1.03
    if i >= 9:
        continue
    total_expenses += expenses
    if i > 1:
        continue
    total_expenses += expenses
else:
    print('Студенту надо попросить', round(total_expenses), 'рублей')
