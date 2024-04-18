# Sukurkite Calculator klasę su pagrindinėmis funkcijomis:
# sudėti, dalyti, dauginti, atimti ir t. t.. Inicijuokite klasę ir parodykite keletą skaičiavimų.

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError(" Dalyba is nulio negalima! ")

calculate = Calculator()

x = int(input("pirmas skaicius "))
y = int(input("antras skaicius "))


print(calculate.add(x, y))
print(calculate.multiply(x, y))
print(calculate.subtract(x, y))
print(calculate.divide(x, y))

# Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas).
# Turint asmens vardą ir pavardę:
#
# Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę, atskiriamus tarpeliu.
#
# Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį .
# Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.


class Worker:
    def __init__(self, name: str, surname: str):
        self.fullname = f"{name} {surname}"
        self.email = f"{name.lower()}_{surname.lower()}@company.com"


worker = Worker("Tomas", "Sapiega")


print(worker.fullname)
print(worker.email)


# Sukurkite knygos klasę Book, kuri turi du atributus: name , author, ir du metodus:
# Metodas, pavadintas .get_title(), kuris grąžina: "Pavadinimas: " + egzemplioriaus pavadinimas.
# Metodas .get_autor(), kuris grąžina: "Autorius: " + egzempliorius autorius.
# ir instancuokite šią klasę sukurdami 3 naujas knygas:
# Pride and Prejudice - Jane Austen (PP)
# - Hamletas - Viljamas Šekspyras (H)
# - Karas ir taika - Levas Tolstojus (WP)
# Naujų egzempliorių pavadinimai turėtų būti atitinkamai PP, H ir WP.
# Pavyzdžiui, jei, naudodamas šią knygų klasę, instancuočiau šią knygą:
# - Haris Poteris - J. K. Rowling (HP)
# Gaučiau šiuos atributus ir metodus:
#
# HP.title ➞ "Harry Potter"
# HP.author ➞ "J.K. Rowling"
# HP.get_title() ➞ "Pavadinimas: Haris Poteris"
# HP.get_author() ➞ "Autorius: Rowling"

class Book:

    def __init__(self, name: str, author: str, series: str):
        self.name = name
        self.author = author
        self.series = series


    def get_title(self):
        return "Title : " + self.name

    def get_author(self):
        return "Author : " + self.author

    # Sukurkime knygą
book_1 = Book("Pride and Prejudice", "Jane Austen", "PP")
book_2 = Book("Hamletas", "Viljamas Šekspyras", "H")
book_3 = Book("Karas ir taika", "Levas Tolstojus", "WP")
book_4 = Book("Haris Poteris", "J. K. Rowling", "HP")

print(book_1.get_title())
print(book_1.get_author())
print(book_2.get_title())
print(book_2.get_author())
print(book_3.get_title())
print(book_3.get_author())
print(book_4.get_title())
print(book_4.get_author())


# Apie šalį galima sakyti, kad ji yra didelė, jei ji yra:
# Didelė gyventojų skaičiumi.
# Didelė pagal plotą.
# Šalies klasę papildykite taip, kad joje būtų atributas is_big.
# Nustatykite jį į True, jei tenkinamas kuris nors iš šių kriterijų:
# Gyventojų skaičius yra didesnis nei 20 mln.
# Plotas didesnis nei 3 mln. km².
# Taip pat sukurkite metodą, kuris palygintų šalies gyventojų tankį su kitos šalies objektu.
# Grąžinkite tokio formato eilutę:
# {country} has a {smaller / larger} population density than {other_country}
# Pavyzdys:
# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)
# australia.is_big ➞ True
# andorra.is_big ➞ False
# andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"

class Country:

    def __init__(self, name: str, population: int, area_size: int ):
        self.name = name
        self.populiation = population
        self.area_size = area_size
        self.is_big = population > 20000000 or area_size > 30000000
        self.density = population / area_size

    def compare_pd(self, name_2):
        if self.populiation / self.area_size > name_2.population / name_2.area_size:
            print(f"{self.name} has a larger population density than {name_2} ")
        else:
            print(f"{self.name} has a smaller population density than {name_2}")
        return name_2.population
`


andora = Country("Andorra", 76098, 468)
australia = Country("Australia", 23545500, 7692024)
ltu = Country('Lithuania',  2886515, 65300)


ltu.compare_pd(australia)
print(ltu.compare_pd(australia))

#andora.compare_pd(australia)
#print(ltu.compare_pd(australia))

#ltu.compare_pd(andora)
#print(ltu.compare_pd(andora))