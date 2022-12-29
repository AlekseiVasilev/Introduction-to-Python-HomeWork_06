# 5 - Есть список случайных чисел в промежутке от 1 до 200, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

list_numbers = [1,1,1,1]

def selection(element):
    if element[0] != element[1]: return True
    else: return False

tuple_numbers = list(enumerate(list_numbers))

mod_tuple_numbers = [element for element, element in enumerate(tuple_numbers) if selection(element)]

print(f'{list_numbers}, -> {tuple_numbers}, -> {mod_tuple_numbers}')
