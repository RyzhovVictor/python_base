# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if user_input == '1':
    print('В месяце 31 день')
elif user_input == '2':
    print('В месяце 28 дней')
elif user_input == '3':
    print('В месяце 31 дней')
elif user_input == '4':
    print('В месяце 30 дней')
elif user_input == '5':
    print('В месяце 31 дней')
elif user_input == '6':
    print('В месяце 30 дней')
elif user_input == '7':
    print('В месяце 31 дней')
elif user_input == '8':
    print('В месяце 31 дней')
elif user_input == '9':
    print('В месяце 30 дней')
elif user_input == '10':
    print('В месяце 31 дней')
elif user_input == '11':
    print('В месяце 30 дней')
elif user_input == '12':
    print('В месяце 31 дней')
else:
    print('Введенное значение не распознано, пожалуйста, введите номер месяца от 1 до 12')




