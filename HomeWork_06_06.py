# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

tuple_numbers = [(10,25),(3,4),(4,1)]

def selection(element):
    if (element[0] + element[1]) % 5: return False
    else: return True

mod_tuple_numbers = [element for element, element in enumerate(tuple_numbers) if selection(element)]

print(f'{tuple_numbers} => {mod_tuple_numbers}')
