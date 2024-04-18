# Sukurkite paprastą programą, kuri registruotų (logs) visus įvesties duomenis iš terminalo.
# Konfigūracijose turi būti rodomi visi papildomi duomenys (laikas, data, lygis ir t. t.).

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logas.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

logger = logging.getLogger()
def get_log():
    x = int(input('skaicius'))
    for i in range(x):
        print(i)
    logger.info(x)
    logger.info(f'cycle')


print(get_log())


# Parašykite funkciją, kuri perkeltų visus vieno tipo elementus į list galą:
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# # Move all the 1s to the end of the array.
# Registruokite įvestis ir rezultatus į failą.

def list_mover(listas, one):
    logger.info(f'pradinis sarasas :{listas}')
    counting = listas.count(one)

    for _ in range(counting):
        listas.remove(one)
        listas.append(one)
    return listas



# Sukurkite apskaitos programą , kuri paimtų metines pajamas, išlaidas, PVM tarifą (visos reikšmės turi būti kintamos)
# ir apskaičiuotų pelną, sumokėtus mokesčius 4 skirtingomis valiutomis (USD, EU, JPY, CNY).
# Visi skaičiavimai ir rezultatai turėtų būti spausdinami ekrane.
# Visi duomenys ir galimos klaidos turi būti registruojami į failą.

logging.basicConfig(level=logging.DEBUG,
                    filename='logas_apskaita.log',
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')

def count_money(met_paj, met_isl, pvm_proc):
    try:
        pelnas = met_paj - met_isl
        mok_pvm = pelnas * pvm_proc
        return pelnas, mok_pvm
    except TypeError as e:
        logging.error(f'TypeError klaida: {e}')
        return 'Turi buti naudojami skaiciai'

def count_dif_cash(pelnas, pvm_proc, usd, cny, jpy):
    try:
        euro_tax = pelnas * pvm_proc
        usd_tax = euro_tax * usd
        cny_tax = euro_tax * cny
        jpy_tax = euro_tax * jpy
        usd_paj = met_paj * usd
        cny_paj = met_paj * cny
        jpy_paj = met_paj * jpy
        usd_isl = met_isl * usd
        cny_isl = met_isl * cny
        jpy_isl = met_isl * jpy

        return euro_tax, usd_tax, cny_tax, jpy_tax, usd_isl, usd_paj, cny_isl, cny_paj, jpy_isl, jpy_paj
    except Exception as e:
        logging.error(f'Ivyko klaida: {e}')

def print_counting(pelnas, mok_pvm, usd_tax, cny_tax, jpy_tax, usd_isl, usd_paj, cny_isl,
                   cny_paj, jpy_isl, jpy_paj):
    usd_prof = usd_paj - usd_isl
    cny_prof = cny_paj - cny_isl
    jpy_prof = jpy_paj - jpy_isl

    print(f"""Euro -  Pelnas yra {met_paj} - {met_isl} = {pelnas}. PVM mokestis yra {euro_tax} """)
    print(f"""USD -  Pelnas yra ({usd_paj} - {usd_isl}) = {usd_prof} .
     PVM mokestis yra {usd_prof} * {pvm_proc} = {usd_tax} """)
    print(f"""CNY -  Pelnas yra ({cny_paj} - {cny_isl}) = {cny_prof} .
         PVM mokestis yra {cny_prof} * {pvm_proc} = {cny_tax} """)
    print(f"""JPY -  Pelnas yra ({jpy_paj} - {jpy_isl}) = {jpy_prof} .
         PVM mokestis yra {jpy_prof} * {pvm_proc} = {jpy_tax} """)
    logging.info(print_counting())




pvm = int(input("PVM TARIFAS procentais - "))
p = str(pvm)
pvm = "0." + p
print(pvm)
pvm_proc = float(pvm)
met_paj = float(input("METINES PAJAMOS EURAIS - "))
met_isl = float(input("METINES ISLAIDOS EURAIS - "))
eu = 1.0
usd = 1.0867
cny = 7.8514
jpy = 164.6142

logging.info(print_counting())

pelnas, mok_pvm = count_money(met_paj, met_isl, pvm_proc)

euro_tax, usd_tax, cny_tax, jpy_tax, usd_isl, usd_paj, cny_isl, cny_paj, jpy_isl, jpy_paj = count_dif_cash(
    pelnas, pvm_proc, usd, cny, jpy)

print_counting(pelnas, mok_pvm, euro_tax, usd_tax, cny_tax, jpy_tax, usd_isl, usd_paj, cny_isl,
                   cny_paj, jpy_isl, jpy_paj)

