import time

lkl = ('Zalgiris' , 'Rytas' , 'Siauliai')
nkl = ('Olimpas', )
lkl_nkl = lkl + nkl
lkl_nkl2 = ('Zalgiris', 'Rytas', 'Siauliai', 'Olimpas')
print(lkl)
print(lkl_nkl2)

# listas
lkl = ['Rytas' , 'zalgiris']
print(lkl)
lkl.append('Siauliai') # kelti po viena , neleidzia 2+
print(lkl)
lkl.insert( 2 ,'Wolves')
print(lkl)
lkl2024 = tuple(lkl)
print(lkl2024)
# print(len(lkl))
# print(lkl.count('Wolves'))
lkl.remove('Wolves')
print(lkl)
lkl.pop(-1)
print(lkl)
del lkl[1]
print(lkl)


battles=['1236', '1260' , '1410' , '1893']
print(battles)
from draftas import  battles   #importas is kito failo , * reiskia visi failai
print(battles)
battles.remove(battles[-1])
print(battles)
lkl.extend(battles)
print(lkl)
print(len(lkl))
tuple_number = tuple(battles)
#  print(battles)
# int_numbers = int(tuple_battles)
# print(tuple_number)

battles.append('1918')
number = []
# for x in battles:
   # print(x) # x generacijos procesas
   # number.append(int(x))
print(number)
print(type(number))
# print(min(number), max(number))
print()
skaiciai = [2 , 5 ,8 ,11 , 14 ,17]
for x in battles:
    print('Musis', x)
for x in skaiciai:
    print(x , x + 3)

my_list = ['first' , 'second' , 'third']
print(my_list[-1])
print(my_list[:1])
print(my_list[::1])
print(my_list[::-1])
print(my_list[0:2])
print(1 in my_list)

mixas = [5 , 5.6 ,'Lietuva' , [3 , 6.7 , '123'], True]
battles_tuple = list(('1236', '1260' , '1410' , '1893'))
print(mixas)
print(battles_tuple)
for x in lkl:
    print(x + ' lkl Komanda')

lkl.append('Banga')
lkl[2] = 'Olimpas'
print(lkl)

print('Zemaitija' in mixas) # false , nera zemaitijos
print(5 not in mixas) # false , yra 5

print(battles)
if 123 in battles:
    print('Radome skaiciu')
time.sleep(0) # pauze tarp ieskojimu
if '1918' in battles:
    print('Radome data')


number = [5 , 7 , 55 ,878]
print(sum(number))
print()

battles.append('1990')
battles.insert(6 , '1323')

print(battles)


for y in enumerate(battles):
    print(y)


for x in range(len(battles)):
    print(x , battles[x])
    print(x + 1 , battles[x])







import random
import time
nmbrs = [] # tuscias ciklas
for i in range(25):
    # time.sleep(3)
    number.append(random.randint(2 , 200))
   # print(i)
print(number)

number.sort() # rikiavimas is eiles
print(number)
number.reverse() # didziausias > maziausias
print(number)