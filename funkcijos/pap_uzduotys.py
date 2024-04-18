# Reikia parašyti funckiją, kuri turėtų du variable – vienas yra listas, kitas – iš kokio
# skaičiaus reikia kad dalintusi. Reikia grazinti visus skaicius kurie dalinasi is duoto skaiciaus.

def get_list(numbers, digit):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i)
    return answer

numbers = [ 1, 3, 78, 42, 54, 456]
digit = 2


rez = get_list(numbers, digit)

print(rez)


# Parašyti funciją, į kurią padavus skaičių atspausdintų tokia tvarka kaip parodyta žemiau. Funkcija turi priimti 2 variable – nuo kurio iki kurio skaiciaus.:
#
# 1
#
# 22
#
# 333
#
# 4444
#
# 55555
#
# Pvz jei nuo 3 iki 5, spausdina:
# 333
#
# 4444
#
# 55555


def get_range(x, y):
    for i in range(x ,y +1):
        print(str((i)) * i)

x = 3
y= 5

answr = get_range(x, y)

print(answr)


# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def extraxt_in_reverse_order(a):
    a = str(a)
    negative_a = (a[::-1])
    for i in negative_a:
        print(i, end=' ')


a = 7536

print(extraxt_in_reverse_order(a))


# Exercise 13: Print multiplication table from 1 to 10
#
# Expected Output:
#
#
#
# 1  2 3 4 5 6 7 8 9 10
#
# 2  4 6 8 10 12 14 16 18 20
#
# 3  6 9 12 15 18 21 24 27 30
#
# 4  8 12 16 20 24 28 32 36 40
#
# 5  10 15 20 25 30 35 40 45 50
#
# 6  12 18 24 30 36 42 48 54 60
#
# 7  14 21 28 35 42 49 56 63 70
#
# 8  16 24 32 40 48 56 64 72 80
#
# 9  18 27 36 45 54 63 72 81 90
#
# 10 20 30 40 50 60 70 80 90 100


def multiply():
    for d in range(1, 11):
        print(' '.join(f"{d*j:4}" for j in range(1, 11)))



print(multiply())


# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
#
# * * * * *
#
# * * * *
#
# * * *
#
# * *
#
# *

def asterisk(sign):
    for i in range(sign, 0, -1):
        for a in range(0, i):
            print('*', end=' ')
        print()


sign = 5

print(asterisk(sign))






# Pvz. jei duota:
#
# Data = {
#
# 1: ‘vienas’,
#
# 2: ‘du’,
#
# 3: ‘trys’,
#
# 4: ‘keturi’
#
# }
#
# Reikaling = [1, 2]
#
# Trinti = [3]
#
# Grazina du dictus:
#
# {
#
# 1: ‘vienas’,
#
# 2: ‘du’,
#
# 4: ‘keturi’
#
# }
#
# Ir:
#
# {
#
# 1: ‘vienas’,
#
# 2: ‘du’,
#
# }


def play_with_dict(data):
    no_three = {}
    out = [3]
    for key in data:
        if key in data not in out:
            no_three[key]
    return no_three






d = {
    1: 'vienas',2: 'du',
    3: 'trys',4: 'keturi',
}



    # 8. Parasyti funckija, kuri priimtu du vairabe – lista kartotini. Grazinti turi lista, kuriame buvo listai su kartotiniu nariu skaiciumis. Pvz.
#
# Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Kartotinis = 3
#
#
#
# Grazina [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



#def get_stuff_done():
   # new = []
   # for i in range(data , 3):



# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# kartotinis = 3



# d.versija

import math


def return_sliced_list(numbers: list, number : int):
    if not isinstance(numbers, list) or not isinstance(number, int):
        raise TypeError('wrong data type')
    return [numbers[i * number:i * ]]









