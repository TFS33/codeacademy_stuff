# Sukurkite keletą savo pavyzdžių, kuriuose parodytumėte ir panaudotumėt keletą OOP paradigmų praktikoje.



# Parašykite klasę CoffeeShop, kuri turi tris inicializuotos klasės kintamuosius:
#
# name: str (iš esmės parduotuvės pavadinimas)
#
# meniu : elementų sąrašas (list) (dict tipo), kuriame kiekvienas elementas turi elementą (elemento pavadinimą), tipą (ar tai maistas, ar gėrimas) ir kainą.
#
# orders: tuščias list
#
# ir septyni metodai:
#
# add_order: į užsakymų sąrašo pabaigą įtraukia prekės pavadinimą, jei jis yra meniu, priešingu atveju grąžina "Šiuo metu šios prekės nėra!".
#
# fulfill_order: jei užsakymų sąrašas nėra tuščias, grąžinama "{prekė} yra paruošta!". Jei užsakymų sąrašas tuščias, grąžinkite "Visi užsakymai įvykdyti!".
#
# list_orders: grąžina priimtų užsakymų prekių pavadinimus, priešingu atveju - tuščią sąrašą.
#
# due_amount: grąžina bendrą mokėtiną sumą už priimtus užsakymus.
#
# cheapest_item: grąžina pigiausio meniu elemento pavadinimą.
#
# drinks_only: grąžina tik meniu gėrimų tipo elementų pavadinimus.
#
# food_only: grąžina tik meniu maisto tipo elementų pavadinimus.

class CoffeeShop:

    def __init__(self, name: str = 'Beans', meniu ,):
        self.name = name
        self.meniu = meniu
        self.orders = []

    def add_order(self, item):
        for element in self.meniu:
            if element['name'] ==item:
                self.orders.append(item)
                print("Your's order of {item} is acapted")
        return "Šiuo metu šios prekės nėra!"



    def get_fullfill_order(self):
        if self.orders:
            item = self.order.pop(0)
            print(f"{item}') is prepared")
        else:
            print('Order is done')

    def list_order(self):

    def due_amount(self):

    def get_cheapest_item(self):
        cheapest = min(self.meniu, key=lambda x: x["price"])
        return

    def drinks_only(self):

    def food_only(self):


meniu = [
    {'name': 'Coffee', 'type': 'drink', 'price': 2.50},
         {'name': 'Sandwich', 'type': 'food', 'price': 5.00},
        {'name': 'Tea', 'type': 'drink', 'price': 2.00}
]