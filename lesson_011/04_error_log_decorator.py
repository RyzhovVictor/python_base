# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

def file_name(name):
    def log_errors(func):
        def surrogate(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ZeroDivisionError as zero_error:
                file_1 = f'{func.__name__}: |{kwargs}| {Exception} {zero_error}\n'
                with open(name, 'a', encoding='utf8') as file:
                    file.write(file_1)
                raise ZeroDivisionError

            except ValueError as value_error:
                file_2 = f'{func.__name__}: |{args}| {Exception} {value_error}\n'
                with open(name, 'a', encoding='utf8') as file:
                    file.write(file_2)
                raise ValueError

        return surrogate

    return log_errors


# Проверить работу на следующих функциях
@file_name(name='perky.log')
def perky(param):
    return param / 0


@file_name(name='function_errors.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
