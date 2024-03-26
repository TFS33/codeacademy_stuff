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

tm1year = int(1964)
tm2year = int(1999)
tm3year = int(2022)
tm4year = int(1964)
tm5year = int(1999)

arena1 =int(2500)
arena2 = int(2200)
arena3 = int(10000)
arena4 = int(5950)
arena5 = int(1500)

#str
str1 = team1 , tm1city ,tm1year ,arena1
str2 = team2 , tm2city ,tm2year ,arena2
str3 = team3 , tm3city ,tm3year ,arena3
str4 = team4 , tm4city ,tm4year ,arena4
str5 = team5 , tm5city ,tm5year ,arena5

# tuple

tuplesas1 = ((team1 , tm1city ,tm1year ,arena1))
tuplesas2 = ((team2 , tm2city ,tm2year ,arena2))
tuplesas3 = ((team3 , tm3city ,tm3year ,arena3))
tuplesas4 = ((team4 , tm4city ,tm4year ,arena4))
tuplesas5 = ((team5 , tm5city ,tm5year ,arena5))

# listas

list1 = [team1 , tm1city ,tm1year ,arena1]
list2 = [team2 , tm2city ,tm2year ,arena2]
list3 = [team3 , tm3city ,tm3year ,arena3]
list4 = [team4 , tm4city ,tm4year ,arena4]
list5 = [team5 , tm5city ,tm5year ,arena5]

# skirtingi stringai
print(tuplesas1)
print(team2 , ' kuris yra ' , tm2city , ' mieste , ir ikurtas ' , tm2year , ' metais . Arena talpina - ' , arena2 , 'zmoniu.' )
print(list3)

# upper
print(team4.upper() , tm4city.upper(), tm4year , arena4)
#lower
print(team4.lower() , tm4city.lower(), tm4year , arena4)

# 8 . metai
amzius1 = 2024 - tm1year
amzius2 = 2024 - tm2year
amzius3 = 2024 - tm3year
amzius4 = 2024 - tm4year
amzius5 = 2024 - tm5year
pridetis1 = tm1year + 7
daug1 = tm1year * 7
print(amzius1)
print(daug1)


