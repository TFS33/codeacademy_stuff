
print(".........10 uzduotis - elementu suskaiciavimas.......")
print()
tuplesas1 = ("Rytas", "CBET", "Wolves", "Lietkabelis", "Pieno zvaigzdes")
tuplesas2 = ("Vilniaus", "Jonavos", "Vilniaus", "Panevezio", "Pasvalio")
tuplesas3 = (1964, 1999, 2022, 1964, 1999)
tuplesas4 = (2500, 2200, 10000, 5950, 1500)

print(len(tuplesas1))
print(len(tuplesas2))
print(len(tuplesas3))
print(len(tuplesas4))

print("......11 UZDUOTIS atrinkti keturiais elementais duomenis.......")
print()
indeksas = tuplesas1.index("Rytas")
print(indeksas)
print("Vilniaus" in tuplesas2)
print(tuplesas3.count(1999))
print(tuplesas4[3])
print()
print("......uzduotis 12 istraukti seniausia komanda , istraukti didziausia arena.....")

seniausia = min(tuplesas3)
print(seniausia)
didarena = max(tuplesas4)
print(didarena)
print()

stringas1 = "*".join(tuplesas1)
print(
    ".....uzduotis 13 ar tikrai jie prasideda ir pasibaigia jūsų pasirinktais elementų pavadinimais....."
)
print(stringas1.startswith("Rytas"))
print(stringas1.endswith("Rytas"))
print()
print(".......14 uzduotis Išskleidžiame apjungtus TUPLE elementus su ciklu FOR.......")
for x in tuplesas1:
    print(x)
print(".......15 uzduotis atskirti printu - atlikta.......")