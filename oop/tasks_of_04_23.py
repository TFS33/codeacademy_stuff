# Funkcija, kurioje vairable yra args ir kwargs.
#
# Args – intergeris
# Kwargs - string
#
# Grazinkite args’u kvarduru suma
#
# Kwargsuose, atspausdinti key – zodzio ilgio skaicius, valuje – zodziai liste.


def count_result(**kwargs):
    result = {}
    for value in kwargs.values():
        key = len(value)
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    return result


data = {
    "1": "namas",
    "2": "Tadas",
    "3": "Pele",
    "4": "suo",
    "5": "api",
}
print(count_result(**data))


# Write a Python program to find if a given string starts with a given character using Lambda.
# Output:True or False


def get_answer_if_string_begins_with_certain_char(
    string_as,
):
    answer = lambda string, char: string_as.startswith(char)
    return answer(string_as, char)


string_as = "as bas Mas"
char = "a"

result = get_answer_if_string_begins_with_certain_char(string_as)

print(result)

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.


number = lambda i: i + 15

print(number(10))

stuff_two = lambda x, y: x * y

print(stuff_two(10, 2))


# Write a Python program to square and cube every number in a given list of integers using Lambda


def get_sq_and_qb(numbers_in_list):
    sq_and_qb = lambda i: (i, i**2, i**3)
    return [sq_and_qb(i) for i in numbers_in_list]


numbers_in_list = [
    1,
    2,
    3,
    4,
    5,
]

print(get_sq_and_qb(numbers_in_list))

# Write a Python program to extract year, month, date and time using Lambda


from datetime import datetime

a = datetime.now()

year = lambda i: i.year
month = lambda i: i.month
day = lambda i: i.day
time = (
    lambda i: i.time()
)  # be skliaustu gausiu <built-in method time of datetime.datetime object at 0x000001FC70D539F0>

print(year(a))
print(month(a))
print(day(a))
print(time(a))

# Write a Python program to sort a list of tuples using Lambda.

list_of_tuples = [(5, "a"), (1, "b"), (3, "c")]
print(list_of_tuples)

sorted_list = sorted(list_of_tuples, key=lambda i: i[0])

print(sorted_list)

# Write a Python program to sort a list of dictionaries buy color value using Lambda

list_of_dicts = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]

print(list_of_dicts)

sorted_list_two = sorted(list_of_dicts, key=lambda i: i["color"])

print(sorted_list_two)


# Write a Python program to sort a given matrix in ascending order
# according to the sum of its rows using lambda.
def sort_list_inide_list(og_matrix):
    return sorted(og_matrix, key=lambda i: sum(i))


og_matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

print(sort_list_inide_list(og_matrix))
