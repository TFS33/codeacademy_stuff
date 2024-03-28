# Sukurkite programą, kuri leistų naudotojui įvesti skaičių seriją ir apskaičiuotų visų skaičių vidurkį.
# Programa taip pat turėtų išspausdinti visų skaičių list'a ir vidurkį.

numbers_lot = input('Įveskite skaičių seriją, atskirtą tarpu: ')


numbers = [int(a) for a in numbers_lot.split()]


if len(numbers) == 0:
    print('Kur skaiciai?.')
else:

    avg = sum(numbers) / len(numbers)
    print('Visu skaiciu sararas:', numbers)
    print('Vidurkis:', avg)



