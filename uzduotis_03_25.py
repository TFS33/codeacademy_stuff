first = [
    68,
    "Asia",
    5.5,
    False,
    True,
    [
        85,
        55,
    ],
]
print(first)

for value in first:
    print(type(value))

print()

for value in first:
    print(value, "|", type(value))
# Sukurkit list su float tipo duomenimis, turinčius 3 skaitmenis po kablelio. Sukurkite kitą list su visomis reikšmėmis, suapvalintomis iki 2 ženklų po kablelio. Atspausdinkit abiejus list.
print()
second = [5.222, 8.245, 4.182]
rounded_second = [round(num, 2) for num in second]
print(second)
print(rounded_second)
print()

second = [5.222, 8.245, 4.182]
third = []
for n in second:
    # third.append(n)
    # print(n)
    # print(second, third)
    third.append(round(n, 2))

print(second, third)

# Sukurkite list su mokinių vardais ir juos surūšiuokite, rezultatą išspausdinkite į terminalą.

names = ["Tomas", "Laura", "Andrius", "Leonidas"]
names_sorted = sorted(names)
print(names_sorted)

# Parašykite programą, kuri leistų vartotojui įrašyti bet kokį kintamąjį skaičių ir jį suapvalinti iki tam tikro skaičiaus po kablelio.
number = float(input("Iveskite skaiciu pvz 1.222 -"))
rounded_number = round(number, 2)
print(rounded_number)

# data = [‘vienas’, ‘du’, (1, 2, 3), [1, 4, 7], 8, 18, 22, 23.0]
# atspaustindi dicta, kuriame raktas turetu buti tipas, o value skaicius kartu koks duomenu tipas buvo panaudotas.

data = ["vienas", "du", (1, 2, 3), [1, 4, 7], 8, 18, 22, 23.0]
result = {}

for d in data:
    print(d)
    print(type(d))
    data_type = type(d)
    if data_type in result:
        result[data_type] += 1
    else:
        result[data_type] = 1
print(result)
# Yra listas su skaiciais. Atpausdintkite lyginiu skaiciu suma, o nelyginiu skaiciu kvadratu suma

numbers = [1, 2, 3.2, 45, 22]  # list(range(100))

result = {
    "nelyginis": 0,
    "lyginis": 1,
}
for n in numbers:
    if n % 2 == 0:
        result["lyginis"] += n
    else:
        result["nelyginis"] += n**2
print(result)
