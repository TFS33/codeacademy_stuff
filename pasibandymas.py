print('“...........1 uzduotis..........“')
print()
# Aprasymai
team1 = 'Rytas'
team2 = 'CBET'
team3 = 'Wolves'
team4 = 'Lietkabelis'
team5 = 'Pieno zvaigzdes'

tm1city = 'Vilniaus'
tm2city = 'Jonavos'
tm3city = 'Vilniaus'
tm4city = 'Panevezio'
tm5city = 'Pasvalio'

tm1year = 1964
tm2year = 1999
tm3year = 2022
tm4year = 1964
tm5year = 1999

arena1 = 2500
arena2 = 2200
arena3 = 10000
arena4 = 5950
arena5 = 1500
# Komandu duomenys Tuple sarase ir ju isvedimas
print("""
/ Komandos / Komandos    / Ikurimo / Arenos /
/ Miestas  / Pavadinimas / Data    / Vietos /""")
komanda1 = (( team1 , tm1city, tm1year , arena1 ))
komanda2 = (( team1 , tm1city, tm1year , arena1 ))
komanda3 = (( team1 , tm1city, tm1year , arena1 ))
komanda4 = (( team1 , tm1city, tm1year , arena1 ))
komanda5 = (( team1 , tm1city, tm1year , arena1 ))
print(komanda1)
print(komanda2)
print(komanda3)
print(komanda4)
print(komanda5)
print()
# skirtingi formatavimai (su kintamuoju, nukeliant tekstą ir pan. bei panaudojant str , int ir float)
tm4yearf = float(tm4year)
arena4f = float(arena4)

eilute1 = (f'{tm1city} {team1} ikurtas {tm1year}m. bei kurio arena talpina {arena1} asmenu')
eilute2 = (f"""{tm2city} {team2} ikurtas
{tm2year}m. bei kurio arena talpina
{arena2} asmenu""")
eilute3 = tm3city + ' ' + team3 + ' ikurtas ' +str(tm3year) + 'm. bei kurio arena talpina ' + str(arena3) + ' asmenu'
eilute4 = tm4city + ' ' + team4 + ' ikurtas ' + str(tm4yearf) + 'm. bei kurio arena talpina ' + str(arena4f) + ' asmenu'
eilute5 =(f'{tm5city} {team5} ikurtas {tm5year}m. ')
eilute6 =(f'bei kurio arena talpina ' + str(arena5) + ' asmenu')
eilute7 = str(eilute5) + str(eilute6)
print(eilute1)
print(eilute2)
print(eilute3)
print(eilute4)
print(eilute7)
print()
# upper lower
upp1 = tm1city.upper() + ' ' + team1.upper() + ' ikurtas ' +str(tm1year) + 'm. bei kurio arena talpina ' + str(arena1) + ' asmenu'
upp2 = tm2city.upper() + ' ' + team2.upper() + ' ikurtas ' +str(tm2year) + 'm. bei kurio arena talpina ' + str(arena2) + ' asmenu'
upp3 = tm3city.upper() + ' ' + team3.upper() + ' ikurtas ' +str(tm3year) + 'm. bei kurio arena talpina ' + str(arena3) + ' asmenu'
upp4 = tm4city.upper() + ' ' + team4.upper() + ' ikurtas ' +str(tm4year) + 'm. bei kurio arena talpina ' + str(arena4) + ' asmenu'
upp5 = tm5city.upper() + ' ' + team5.upper() + ' ikurtas ' +str(tm5year) + 'm. bei kurio arena talpina ' + str(arena5) + ' asmenu'
print('UPPERCASE')
print(upp1)
print(upp2)
print(upp3)
print(upp4)
print(upp5)
print()
print('lowercase')
low1 = tm1city.lower() + ' ' + team1.lower() + ' ikurtas ' +str(tm1year) + 'm. bei kurio arena talpina ' + str(arena1) + ' asmenu'
low2 = tm2city.lower() + ' ' + team2.lower() + ' ikurtas ' +str(tm1year) + 'm. bei kurio arena talpina ' + str(arena1) + ' asmenu'
low3 = tm3city.lower() + ' ' + team3.lower() + ' ikurtas ' +str(tm1year) + 'm. bei kurio arena talpina ' + str(arena1) + ' asmenu'
low4 = tm4city.lower() + ' ' + team4.lower() + ' ikurtas ' +str(tm1year) + 'm. bei kurio arena talpina ' + str(arena1) + ' asmenu'
low5 = tm5city.lower() + ' ' + team5.lower() + ' ikurtas ' +str(tm1year) + 'm. bei kurio arena talpina ' + str(arena1) + ' asmenu'
print(low1)
print(low2)
print(low3)
print(low4)
print(low5)
print()
# skaiciavimas
print('“...........vis dar 1 uzduotis..........“')
# kiek metu komandai?
m1 = 2024 - tm1year
m2 = 2024 - tm2year
m3 = 2024 - tm3year
m4 = 2024 - tm4year
m5 = 2024 - tm5year
print('Kiek komandai metu?')
print(team1 , ' ' , m1 , 'm')
print(team2 , ' ' , m2 , 'm')
print(team3 , ' ' , m3 , 'm')
print(team4 , ' ' , m4 , 'm')
print(team5 , ' ' , m5 , 'm')
print()
# pridetis
pr1 = m1 + 7
pr2 = m2 + 7
pr3 = m3 + 7
pr4 = m4 + 7
pr5 = m5 + 7
# sandauga
daug1 = m1 * 7
daug2 = m2 * 7
daug3 = m3 * 7
daug4 = m4 * 7
daug5 = m5 * 7
# dalyba
dal1 = m1 / 7
dal2 = m2 / 7
dal3 = m3 / 7
dal4 = m4/ 7
dal5 = m5 / 7
# kelimas laipsniu
keliam1 = m1 ** 7
keliam2 = m2 ** 7
keliam3 = m3 ** 7
keliam4 = m4 ** 7
keliam5 = m5 ** 7
# liekana
liek1 = m1 % 7
liek2 = m2 % 7
liek3 = m3 % 7
liek4 = m4 % 7
liek5 = m5 % 7
# visko suma ARBA BELENKOKIO DYDZIO SKAICIUS
belenkas = m1 + pr1 + daug1 + dal1 + keliam1 + liek1 + m2 + pr2 + daug2 + dal2 + keliam2 + liek2 + m3 + pr3 + daug3 + dal3 + keliam3 + liek3 + m4 + pr4 + daug4 + dal4 + keliam4 + liek4 + m5 + pr5 + daug5 + dal5 + keliam5 + liek5
print(belenkas)
print()
# lyginimas naudojant loginius operatorius
logop1 = team1 == team2
logop2 = team2 == team3
logop3 = team3 == team4
logop4 = team4 == team5
logop5 = team1 == team3
print('Komandu pavadinimu palyginimas')
print(logop1 , logop2 , logop3 , logop4 ,logop5)
metop1 = tm1year != tm2year
metop2 = tm2year != tm3year
metop3 = tm3year != tm4year
metop4 = tm4year != tm5year
metop5 = tm5year != tm1year
print('komandu ikurimo metu sutapimas')
print(metop1 , metop2 ,metop3 , metop4 , metop5)
ar1 = arena1 < arena2
ar2 = arena2 < arena3
ar3 = arena3 < arena4
ar4 = arena4 < arena5
ar5 = arena5 < arena1
print('arenos vietu palyginimas(daugiau ar maziau < ')
print(ar1 , ar2 ,ar3 ,ar4 , ar5)
