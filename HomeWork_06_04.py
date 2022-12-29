# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

from gbfunctions import random_list, give_int
import math

def selection(element):
    if sum(list(map(int, (str(element))))) %2 != 1 or sum(list(map(int, (str(element))))) %2 == 0: return True
    else: return False



numbers = give_int('Введите количество элементов списка: \n')
start_list = random_list(numbers)

mod_numbers = [element for element, element in enumerate(start_list) if selection(element)]


print(f'Элементов списка: {numbers}, Список: {start_list}, Итоговый список: {mod_numbers}')