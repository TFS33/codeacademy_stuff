# Parašykite funkciją, kuri paima du list('us ir prie pirmojo list pirmojo elemento prideda antrojo listpirmąjį elementą,
# antrojo sąrašo antrąjį elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo antrąjį elementą.'
# pirmąjį sąrašą su antruoju antrojo sąrašo elementu ir t. t., ir t. t.
# Grąžinkite True, jei visi elementų deriniai sudaro tą patį skaičių. Priešingu atveju grąžinama False.)

def add_seperate_list(first , second) -> list:
    if len(first) != len(second):
        return False

    for i in range(len(first)):
        if first[i] != second[i] * (i + 1):
            return False

    return True


first = [1, 2, 3, 4, 7]
second = [2, 3, 4, 5, 6]

print(add_seperate_list(first, second))


# Tarp lyginių ir nelyginių skaičių vyksta didelis karas. Šiame kare jau žuvo daug skaičių, todėl tavo užduotis - jį nutraukti.
# Jūs turite nustatyti, kurios grupės sumos didesnės: lyginių ar nelyginių. Laimi didesnė grupė.
#
# Sukurkite funkciją, kuri paimtų sveikųjų skaičių sąrašą, atskirai suskaičiuotų lyginių ir nelyginių skaičių sumas,
# tada grąžintų lyginių ir nelyginių skaičių sumų skirtumą skaičių.


def get_numbers_sum(warriors) -> list:
    lyg_skaiciai = []
    nelyg_skaiciai = []
    for i in warriors:
        if i % 2 == 0:
            lyg_skaiciai.append(i)
        else:
            nelyg_skaiciai.append(i)
    lyg_suma = sum(lyg_skaiciai)
    nelyg_suma = sum(nelyg_skaiciai)
    return lyg_suma, nelyg_suma

def get_a_winner(lyg_suma, nelyg_suma) -> list:
    if lyg_suma > nelyg_suma:
        return "Lyginiai laimėjo"
    elif lyg_suma < nelyg_suma:
        return "Nelyginiai laimėjo"
    else:
        return "Laukia antras raundas..."

def get_difference(lyg_suma, nelyg_suma) -> list:
    if lyg_suma > nelyg_suma:
        return lyg_suma - nelyg_suma
    elif lyg_suma < nelyg_suma:
        return nelyg_suma - lyg_suma
    else:
        return "Skaiciai lygūs"



warriors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 33, 55, 66, 77, ]

lyg_suma, nelyg_suma = get_numbers_sum(warriors) # kintamojo isikvietimas, kitaip print neveiks
skirtumas = get_difference(lyg_suma, nelyg_suma)

print(get_a_winner(lyg_suma, nelyg_suma))
print(skirtumas)



# Jums duotas bigramų masyvas ir žodžių masyvas.
# Parašykite funkciją, kuri grąžintų True, jei iš šio masyvo galima rasti kiekvieną bigramą bent vieną kartą žodžių masyve


def check_bigrams(bigrams, words) -> list:
    for bigrams in bigrams:
        if bigrams not in ' '.join(words):
            return False
    return True

bigrams = ["oo", "mi", "ki", "la"]
words = ["milk", "chocolate", "cooks", "cooks"]

print(check_bigrams(bigrams, words))