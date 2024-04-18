# Write a Python program to create a generator that generates the
# squares of numbers up to a given number.


def squares_generator(number):
    for i in range(number + 1):
        yield i ** 2


number = 10

squares = squares_generator(number)

for i in squares:
    print(i)

# Write a Python program to create a generator that
# yields "n" random numbers between a low and high number that are inputs.

from random import randint


def get_random_numbers(low, high, n):
    for _ in range(n):
        yield randint(low, high)


low, high, n = [int(i) for x in input(" 3 skaiciai - ").split()]

nmbrs = get_random_numbers(low, high, n)

for i in nmbrs:
    print(i)


# Write a Python program to create a generator that iterates over a string.

def iter_string(text):
    for i in text:
        yield i


text = "Write a Python program to create a generator that iterates over a string"

it_str = iter_string(text)

for i in it_str:
    print(i)

# Write a Python program to create a Fibonacci series generator.
print()

def fib_gen():
    a = 1
    b = 2

    while True:
        yield b
        a, b = b, a + b

fibo = fib_gen()

print(next(fibo))
print(next(fibo))


# Write a Python program to create a generator from a list
# that yields item from the list if it is a number

print()
def generate_this(x):
    for i in x:
        if isinstance(i, int):
            yield i


a_list = [1, 'q', 2, 'w', 3, 'e', ]

for number in generate_this(a_list):
    print(number)

# Create a list of tuples, each representing a person's information.
# Each tuple contains the following information: (name: str, age: int, city: str, salary: float).
# Your task is to create Python generators to perform the following tasks:
#
# Filtering Generator: Create a generator function that filters the people who are below a certain age threshold.
# Mapping Generator: Create a generator function that maps the names of people to uppercase.
# Aggregation Generator: Create a generator function that calculates the average salary of the selected group.


