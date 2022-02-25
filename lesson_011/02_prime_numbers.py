# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#     def __init__(self, n):
#         self.prime_numbers = []
#         self.n = n
#         self.i = 0
#
#     def __iter__(self):
#         self.i = 1
#         return self
#
#     def get_prime_numbers(self):
#         self.i += 1
#         for prime in self.prime_numbers:
#             if self.i % prime == 0:
#                 return None
#         self.prime_numbers.append(self.i)
#         return self.i
#
#     def __next__(self):
#         value = None
#         while value is None:
#             value = self.get_prime_numbers()
#         if self.i < self.n:
#             return value
#         else:
#             raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

prime_numbers = []


def prime_numbers_generator(n):
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if not number % prime:
                break
        else:
            prime_numbers.append(number)
            yield number


def is_lucky(number):
    number = str(number)
    middle = len(number) // 2
    if sum(map(int, number[:middle])) == sum(map(int, number[-middle:])):
        return True
    else:
        return False


def is_palindrome(number):
    number = str(number)
    reversed_number = number[::-1]
    if number == reversed_number:
        return 'is a palindrome'
    else:
        return 'is not palindrome'


def is_sum(number):
    number = str(number)
    if sum(map(int, number)) in prime_numbers:
        return True
    else:
        return False


for i in prime_numbers_generator(100000):
    print(f'{i} - {is_lucky(i)}, {i} - {is_palindrome(i)}, {i} - {is_sum(i)}')

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
#зачёт!