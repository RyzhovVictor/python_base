# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):

    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


class NotAgeError(Exception):

    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message


def read_line(line_1):
    split_text = line_1.split(' ', 2)
    if len(split_text) == 3:
        name, mail, age = split_text
    else:
        raise ValueError(f'НЕ присутсвует одно или несколько полей')
    try:
        age = int(age)
    except ValueError:
        raise NotAgeError(f'Ошибка в значении возраста')
    if age < 10 or age > 99:
        raise ValueError('поле возраст НЕ является числом от 10 до 99')
    if not name.isalpha():
        raise NotNameError('поле имени содержит НЕ только буквы')
    if '@' not in mail or '.' not in mail:
        raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')

    return True


good_acc = []
bad_acc = []
text = open('registrations.txt', 'r', encoding="utf-8")
for line in text.read().splitlines():
    try:
        if read_line(line):
            good_acc.append(line)
    except Exception as error:
        bad_acc.append(f'{line} | {error}')

with open('registrations_good.log', 'w', encoding='utf-8') as f:
    f.write('\n'.join(good_acc))
with open('registrations_bad.log', 'w', encoding='utf-8') as f:
    f.write('\n'.join(bad_acc))
#зачёт!