#  Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.

numbers = []
for i in range(10):
    numb = int(input('Iveskite 10 skaiciu'))
    numbers.append(numb)
else:
    print('Kazka blogai suvedei')

suma = sum(numbers)
viso = len(numbers)
avg = suma / viso

print(f' suma -{suma}, vidurikis - {avg}')