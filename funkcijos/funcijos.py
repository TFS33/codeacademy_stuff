# Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.
def get_numbers_sum(listas):
    return sum(listas)


listas = [1, 2, 4, 5]
print('Suma : ', get_numbers_sum(listas))


def get_numbers(listas):
    return [number for number in listas if number % 2 == 0]


print(get_numbers(listas))

import random


# def get_random_numbers(a, b, c):
# return [random.randint(a, b, ) for c in range()]


# Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę

def add_smth(listas, galune):
    return [str(smth) + galune for smth in listas]


listas = [1, 2, 3, 'ABC']
galune = 'opapa'

print(add_smth(listas, galune))

#destytojo versija

def add_string(values, end_string = 'string'):
    return [f'{d}_{end_string}' for d in values]

data = [1, 2, 3 , 'namas', ]
end_string = 's'
#print(add_string(values=data, end_string))



# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą

def get_numbers_operations(first, second):
    suma = first + second
    skirtumas = first - second
    daugyba = first * second
    dalyba = first / second
    return suma, skirtumas, dalyba, daugyba

first = int(input('iveskite pirma skaiciu :'))
second = int(input('iveskite pirma skaiciu :'))

results = get_numbers_operations(first, second)

print('suma:', results[0])
print('skirtumas:', results[1])
print('daugyba:', results[2])
print('dalyba:', results[3])


# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes

def get_unique(words) -> str:
    unique = ''
    for unknown in words:
        if unknown not in unique:
            unique += unknown
            return unique

words = 'Buvo senis ir senute, susitarę bulves skutė'

print(get_unique(words))


# Parašykite programą, apibrėžiančią funkciją extract_email_addresses(),
# kuri priima tekstą kaip įvestį ir iš teksto ištraukia visus el. pašto adresus




def extract_email_addresses(text : str):
    splitted_text = text.split()
    e_adress = [word for word in splitted_text if '@' in word and '.' in word]
    return e_adress


text = str(input('Tekstas ='))
email = extract_email_addresses(text)
print(email)








