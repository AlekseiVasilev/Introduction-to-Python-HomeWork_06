# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from gbfunctions import random_list, give_int
import math

numbers = give_int('Введите количество элементов списка: \n')
start_list = random_list(numbers)

mod_numbers = [(start_list[i] * start_list[len(start_list) - 1 - i]) for i in range (int(math.ceil(len(start_list) / 2)))]

print(f'Элементов списка: {numbers}, Список: {start_list}, Список произведений: {mod_numbers}')

