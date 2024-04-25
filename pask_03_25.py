number = int(input("Iveskite skaiciu :"))
if number % 3 == 0 and number % 5 == 0:
    print("FIZZbuzz")
elif number % 5 == 0:
    print("BUZZ")
elif number % 3 == 0:
    print("Fizz")
else:
    print("Nesidalina")

my_list = [45, 20, 14, 55]
sorted_list = sorted(my_list)

print(sorted_list)

sorted_reverse_list = sorted(my_list, reverse=True)

print(sorted_reverse_list)

if type(my_list) is list:
    print("LISTAS")

if isinstance(my_list, list):
    print("LISTAS")

number = 10.155
print(round(number))


def round_numbers(value, decimals):
    print(round(value, decimals))


round_numbers(number)
