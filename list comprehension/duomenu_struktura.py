# Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6


def find_numbers_devide_six():
    result = []
    for number in range(1, 1001):
        if number % 6 == 0:
            result.append(number)
    return result  # [numbers for number in range(1, 1001) if number % 6 == 0]


# Raskite visus skaičius iš 1-1000, kuriuose yra 9
def find_numbers_devide_nines():
    result = []
    for number in range(1, 1001):
        if '9' in str(number):
            result.append(number)
    return result


print(find_numbers_devide_nines())

# Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.

a_lot_of_e = "Buvo senis ir senute, susitarę bulves skutė"


def find_words_with_e():
    result = []
    for word in a_lot_of_e.split():
        if 'e' in word:
            result.append(word)

    return result


print(find_words_with_e())


# Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius, skaičių.

def more_than_five():
    result = []
    for word in a_lot_of_e.split():
        if len(word) >= 6:
            result.append(word)
    return len(result)


print(more_than_five())

# Parašykite programą, kuri patikrintų, ar duotas skaičius yra tobulasis kvadratas.

import math
from math import sqrt


def perf_sq(x):
    sq_root = int(sqrt(x))

    return (sq_root * sq_root) == x


x = int(input("Ivesk skaiciu = "))

print(perf_sq(x))

# Pabandysiu.... Lentynoje sudeti batai:
# [8.90, 4,90, 13,20, 8,80, 14,00, 12,00]
# a) Paskaičiuokite kiek eurų liks žmogui, jei jis šiuo metu pirks dvejus pigiausius batus;
# b) kokius dvejus batus jam nupirkti, jei jis turi 20 eurų ir nori, kad jam liktų kuo mažiau eurų;

#a.

price = [8.90, 4.90, 13.20, 8.80, 14.00, 12.00]

sorted_price = sorted(price)

cheap = sum(sorted_price[:2])

cheap = round(cheap, 2)

leftovers = 20 - cheap
leftovers = round(leftovers, 2)

print(leftovers)

#b.

def shoe_money(shoe, money):
    sorted_shoes = sorted(price)


