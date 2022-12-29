# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

from gbfunctions import give_int
import math

# num = give_int('Введите число: \n')
# numbers_list = give_int('Введите количество элементов списка: \n')

num = -3
numbers_list = 5


degree = list(range(0, numbers_list))

num_degree = [num**degree[i] for i in range(len(degree))]

print(f'Число: {num}, Список степеней: {degree}, Итоговый список последовательности: {num_degree}')

# lambda degree: 
