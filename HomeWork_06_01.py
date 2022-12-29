# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Вам нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# working_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# target_value = "qwe"

# working_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# target_value = "йцу"

# working_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# target_value = "йцу"

# working_list = ["123", "234", 123, "567"]
# target_value = "123"

working_list = []
target_value = "123"

target = [index for index, element in enumerate(working_list) if element == target_value]

if len(target) < 1:
    ansver = 'Вхождений нет'
elif len(target) < 2:
    ansver = 'Второго вхождения нет'
else:
    ansver = ('Позиция второго вхождения искомого значения: ' + str(target[1]))

print(f"Список вхождений: {target}, {ansver}")




# working_list = list(filter(lambda x: x == target_value, working_list))



# Решение с поиском первого вхождения 1:

# my_list = ['b', 'a', 2, 'n', False, 'a', 'n', 'a']

# all_occurrences = [index for index, element in enumerate(my_list) if element == 'a']

# print("The element was found at: " + str(all_occurrences))


# Решение с поиском первого вхождения 2:

# my_list = ['b', 'a', 2, 'n', False, 'a', 'n', 'a']

# all_occurrences = []
# last_found_index = -1
# element_found = True

# while element_found:
#     try:
#         last_found_index = my_list.index('a', last_found_index + 1)
#         all_occurrences.append(last_found_index)
#     except ValueError:
#         element_found = False
    
# if len(all_occurrences) == 0:
#     print("The element wasn't found in the list")
# else:
#     print("The element was found at: " + str(all_occurrences))