def get_numbers_sum(warriors) -> list:
    lyg_skaiciai = []
    nelyg_skaiciai = []
    try:
        for i in warriors:
            if i % 2 == 0:
                lyg_skaiciai.append(i)
            else:
                nelyg_skaiciai.append(i)
    except IndentationError:
        print('Blogas')
    lyg_suma = sum(lyg_skaiciai)
    nelyg_suma = sum(nelyg_skaiciai)
    return lyg_suma, nelyg_suma


def get_a_winner(lyg_suma, nelyg_suma) -> list:

        assert isinstance(nelyg_suma, object)
        if lyg_suma > nelyg_suma:
            return "Lyginiai laimėjo"
        elif lyg_suma < nelyg_suma:
            return "Nelyginiai laimėjo"
        else:
            return "Laukia antras raundas..."


def get_difference(lyg_suma, nelyg_suma) -> list:
    try:
        if lyg_suma > nelyg_suma:
            return lyg_suma - nelyg_suma
        elif lyg_suma < nelyg_suma:
            return nelyg_suma - lyg_suma
        else:
            return "Skaiciai lygūs"
    except IndentationError:
        raise 'Fix a damn code'

try:
    warriors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 33, 55, 66, 77, ]

    lyg_suma, nelyg_suma = get_numbers_sum(warriors)  # kintamojo isikvietimas, kitaip print neveiks
    skirtumas = get_difference(lyg_suma, nelyg_suma)

    print(get_a_winner(lyg_suma, nelyg_suma))
    print(skirtumas)
except KeyboardInterrupt as error:
    print(f"Kodel nutraukei? {error}")




def get_a_fourth_one():
    quotes = {
        "Darth Vader" : "I find your lack of faith disturbing ",
        "Yoda" : "Do or do not. There is no try.",
        "Obi-Wan Kenobi" : "The Force will be with you, always.",
        "Darth Vader" : "I am your father.",
        "Princess Leia" : "Help me, Obi-Wan Kenobi. You’re my only hope",
        "Admiral Ackbar" : "It’s a trap!",
        "Obi-Wan Kenobi" : "in my experience, there is no such thing as luck",
        }
    persons = list(quotes.keys())
    print(persons)
    while True:
        try:
            request = str(input('Enter characters name .... '))
            if request in quotes:
                return quotes[request]
        except KeyboardInterrupt:
            print("I have a bad feeling about this....")


quote = get_a_fourth_one()
print(" ----> ", quote)



# antra uzduotis
"""
Python kalboje, dalijant iš nulio, gauname ZeroDivisionError. 
Jūsų užduotis - sukurti funkciją, kuri:

Kaip argumentus priima du skaičius.

Mėgina padalyti pirmąjį skaičių iš antrojo.

Jei antrasis skaičius yra nulis, ji turėtų sugauti ZeroDivisionError ir grąžinti pasirinktinį klaidos pranešimą.

Jei dalijimas sėkmingas, turėtų būti grąžinamas rezultatas.

Nepriklausomai nuo to, ar dalijimas pavyko, ar ne, turėtų būti išspausdintas pranešimas "Attempted division". 
Jei įvesties duomenys nėra skaičiai, pateikiamas TypeError pranešimas. 
Funkcija pagauna šią TypeError ir grąžina pasirinktinį klaidos pranešimą.
"""


def get_divided(a, b):
    try:
        result = a / b
        print("Attempted division")
        return result
    except ZeroDivisionError:
        print("Dalyba iš nulio negalima")
        return "no zeros.... error message - division by zero not possible"
    except TypeError:
        print('Raides ar zenklai nesidalina')
        return 'You need input numbers....'


a = int(input('iveskite pirma skaičių -'))
b = int(input('iveskite antraji skaičių -'))

print(get_divided(a, b))



# Sukurkite mini "Python" programą, kuri įvestų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
# Tvarkykite visas galimas klaida

def calculate(q, w):
    try:
        sum_ = q + w
        minus = q - w
        minus_two = w - q
        divide = q / w
        divide_two = w / q
        multiply = q * w
        return sum_, minus, minus_two, divide, divide_two, multiply
    except ZeroDivisionError:
        return "Dalyba iŠ NULIO NEGALIMA"
    except TypeError:
        return 'Būtina suvesti skaičius , o ne raides ar ženklus'


def get_input():
    try:
        q = float(input('Pirmas skaicius - '))
        w = float(input('Antras skaicius - '))
        answer = calculate(q, w)
        print(f"Suma = {q} + {w} = {answer[0]}")
        print(f"Skirtumas = {q} - {w} = {answer[1]}")
        print(f"Skirtumas iš kitos puses = {w} - {q} = {answer[2]}")
        print(f"Dalyba = {q} / {w} = {answer[3]}")
        print(f"Dalyba iš kitos puses = {w} / {q} = {answer[4]}")
        print(f"Daugyba = {q} * {w} = {answer[5]}")
    except ValueError:
        print('tina suvesti skaičius , o ne raides ar ženklus')


answer = get_input()

print(answer)

# Atnaujinkite ankstesnę užduotį su galimomis raise išimtimis.

def calculate(q, w):
    try:
        sum_ = q + w
        minus = q - w
        minus_two = w - q
        divide = q / w
        divide_two = w / q
        multiply = q * w
        return sum_, minus, minus_two, divide, divide_two, multiply
    except ZeroDivisionError:
        raise "Dalyba iŠ NULIO NEGALIMA"
    except TypeError:
        raise 'Būtina suvesti skaičius , o ne raides ar ženklus'


def get_input():
    try:
        q = float(input('Pirmas skaicius - '))
        w = float(input('Antras skaicius - '))
        answer = calculate(q, w)
        print(f"Suma = {q} + {w} = {answer[0]}")
        print(f"Skirtumas = {q} - {w} = {answer[1]}")
        print(f"Skirtumas iš kitos puses = {w} - {q} = {answer[2]}")
        print(f"Dalyba = {q} / {w} = {answer[3]}")
        print(f"Dalyba iš kitos puses = {w} / {q} = {answer[4]}")
        print(f"Daugyba = {q} * {w} = {answer[5]}")
    except ValueError as mistake:
        raise ValueError('Butina suvesti skaičius , o ne raides ar ženklus') from mistake


answer = get_input()

print(answer)