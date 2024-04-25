""" Write a Python program to triple all numbers of a given list of integers. Use Python map()"""


def triple_numbers(*args):
    return list(map((lambda i: i * 3), args))


og_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = [2, 4, 6, 8, 10]
odd_numbers_list = [1, 3, 5, 7, 9]
tuple_list = tuple(odd_numbers_list)

print(triple_numbers(*og_list))


# Write a Python program to square the elements of a list using map() function.


def square_numbers_inside_list(*args):
    return list(map((lambda i: i**2), args))


print(square_numbers_inside_list(*og_list))


# Write a Python program to add three given lists using Python map and lambda


def add_three_lists_together(*args):
    return list(map((lambda i: i), args))


print(add_three_lists_together(*og_list, *odd_numbers_list, *even_numbers_list))


# Write a Python program to add two given lists and find the difference between lists. Use map() function.


def add_two_list(*args):
    return map(lambda i, y: i + y, og_list, even_numbers_list)


def compare_list(*args):
    added_list = set(og_list + even_numbers_list)
    print(added_list)
    result = [
        number
        for number in added_list
        if not (number in og_list and number in even_numbers_list)
    ]
    return result


print(list(add_two_list(*og_list, *even_numbers_list)))
print(compare_list(*og_list, *even_numbers_list))

# Write a Python program to convert a given list of integers and a tuple of integers in a list of strings


def convert_list_and_tuple_into_string(*args):
    return "".join(map(str, args))


print(convert_list_and_tuple_into_string(*og_list, *tuple_list))

# Write a Python program to filter a list of integers using Lambda


def get_even_and_odds_from_list(*args):
    evens = list(filter(lambda i: i % 2 == 0, args))
    odds = list(filter(lambda i: i % 2 == 1, args))
    return evens, odds


print(get_even_and_odds_from_list(*og_list))


# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.


def find_numbers(*args):
    return list(filter(lambda i: i % 19 == 0 or i % 13 == 0, args))


org_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(find_numbers(*org_list))

# Write a Python program to count the even, odd numbers in a given array of integers using Lambda.


def count_evens_and_odds(*args):
    even_this = len(list(filter(lambda i: i % 2 == 0, args)))
    odd_this = len(list(filter(lambda i: i % 2 == 1, args)))
    return f"lyginiai {even_this}, nelyginiai {odd_this}"


og_array = [1, 2, 3, 5, 7, 8, 9, 10]

print(count_evens_and_odds(*og_array))

# Use reduce for following tasks
# Write a python program that multiplies all the values in a given list of integers

from functools import reduce


def multiply_values(*args):
    return reduce((lambda i, q: i * q), args)


print(multiply_values(*og_array))

# Write a python program that finds the maximum value within the given list.


def find_max_value(*args):
    return reduce(max, args)


print(find_max_value(*og_array))

# Write a python function that given list of strings concatenates all of them together


def join_list_into_strings(*args):
    return reduce((lambda i, y: i + y), args)


list_of_strings = ["Apple", "Banana", "Orange", "Grapes", "Pineapple"]

print(join_list_into_strings(*list_of_strings))
