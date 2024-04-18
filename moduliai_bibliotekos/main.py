# from funkcijos import buliu_karve # importas
import pyjokes

# eina kartu su modul.py failu

# pirma uzduotis
# Sukurkite paprastą skaičiavimo programą kaip skriptą ir kaip modulį

from modul import counting_numbers

x = int(input("Ivesk skaiciu -"))

print(counting_numbers(x))

# antra uzduotis
# Sukurkite programą su 3 skirtingais moduliais:
#
# Pirma, atlikti pagrindines užduotis su string
#
# antra, pagrindinius uždavinius su list.
#
# trečias, pagrindiniai uždaviniai su float/ int
# Importuokite juos kaip modulius į main.py modulį ir parodykite skaičiavimus.

from modul import capitalize_string

f = "Sukurkite programą su 3 skirtingais moduliais"


print(capitalize_string(f))





# trecia

from modul import get_joke

yeay_or_nay = str(input("yes or no? -"))
if yeay_or_nay == "yes":
    print(get_joke())
else:
    print("Why?")




# ketvirta uzduotis
# "Python" modulis os suteikia galimybę naudotis nuo operacinės sistemos priklausančiomis funkcijomis, pvz., skaityti arba rašyti į failų sistemą. Jūsų užduotis yra:
#
# Importuoti os modulį.
#
# Sukurti funkciją, kuri išvardytų visus dabartiniame kataloge esančius failus.
#
# Sukurti funkciją, kuri sukuria naują katalogą.
#
# Sukurti funkciją, kuri pervadina failą.
#
# Sukurkite funkciją, kuri perkelia failą iš vieno katalogo į kitą.
#
# Sukurkite funkciją, kuri ištrina failą.

