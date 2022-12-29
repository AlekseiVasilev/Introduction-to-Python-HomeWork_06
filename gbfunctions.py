import random
from typing import Optional

def random_list_min_max(list_length, min, max):
    '''
    \n****
    \nAccepts an empty list and the number of elements of the future list,
    \nreturns a list filled with random numbers
    \n****
    \nParameters: list length, minimum and maximum values
    \nReturns: a list of random numbers
    \n****
    '''
    numbers = []
    for i in range(list_length):
        numbers.append(random.randint(min, max))
    return numbers    

def random_list(list_length):
    '''
    \n****
    \nAccepts an empty list and the number of elements of the future list,
    \nreturns a list filled with random numbers
    \n****
    \nParameters: list length
    \nReturns: a list of random numbers
    \n****
    '''
    numbers = []
    for i in range(list_length):
        numbers.append(random.randint(0, 99))
    return numbers    

def give_int(input_string: str,
             min_num: Optional[int] = None) -> int:
    """
    Gives integer number
    :param input_string: welcome to input
    :param min_num: minimum for number's value
    :return: int number
    """

    while True:
        try:
            num = int(input(input_string))
            if min_num and num <= min_num:
                print(f'Type number bigger then {min_num}!')
                continue
            return num
        except ValueError:
            print("That's not a natural number.")
