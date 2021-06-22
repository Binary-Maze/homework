# """
# Домашнее задание №1
# Функции и структуры данных
# Задача №1
# # """
#     функция, которая принимает N целых чисел,
#     и возвращает список квадратов этих чисел
#     >>> power_numbers(1, 2, 5, 7)
#     <<< [1, 4, 25, 49]
#     """
#
#
def power_numbers(list_of_numbers):
    list_of_numb2 = []
    for num in list_of_numbers:
        list_of_numb2.append(num**2)
    return list_of_numb2

numb = power_numbers([1, 2, 5, 7])
print(numb)


## Задача №2
# # filter types
# ODD = "odd"
# EVEN = "even"
# PRIME = "prime"
#
#
# def filter_numbers():
#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только нечётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#
#     >>> filter_numbers([1, 2, 3], ODD)
#     <<< [1, 3]
#     >>> filter_numbers([2, 3, 4, 5], EVEN)
#     <<< [2, 4]
#     """
#

def filter_numbers(list_of_numbers):
    list_of_odd = []
    for num in list_of_numbers:
        if num % 2 != 0:
            list_of_odd.append(num)
    return list_of_odd

numb = filter_numbers([1, 2, 3])
print(numb)

## Задача №3
# # filter types
# ODD = "odd"
# EVEN = "even"
# PRIME = "prime"
#
#
# def filter_numbers():
#     """
#     функция, которая на вход принимает список из целых чисел,
#     и возвращает только чётные/простые числа
#     (выбор производится передачей дополнительного аргумента)
#
#     >>> filter_numbers([1, 2, 3], ODD)
#     <<< [1, 3]
#     >>> filter_numbers([2, 3, 4, 5], EVEN)
#     <<< [2, 4]
#     """
#
def filter_numbers(list_of_numbers):
    list_of_even = []
    for num in list_of_numbers:
        if num % 2 == 0:
            list_of_even.append(num)
    return list_of_even

numb = filter_numbers([2, 3, 4, 5])
print(numb)