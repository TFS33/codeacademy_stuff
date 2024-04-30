x = 10

if x == 10:
    print(x)

x = 500
y = 600

if  x<y:
     print('y yra didesnis uz x')

if  y<x:
     print('x yra didesnis uz y')

x = 900
y = 600
if  x<y:
     print('y yra didesnis2 uz x')

if  y<x:
     print('x yra didesnis2 uz y')

if y < x:
    print('x yra didesnis2 uz y')



import random



x=10
y=11
if  y<x:
     print('x yra didesnis3 uz y')
     x =+ 1
     print(x)

x = random.randint(0 , 10)
y = random.randint(0 , 10)

print(f" Gauta - x {x} ir  - y {y} ")

if  x<y:
     print('y yra didesnis uz x')

if  y<x:
     print('x yra didesnis uz y')

if x==y:
    print( ' x ir y lygus')


x = random.randint(0 , 10)
y = random.randint(0 , 10)

print(f" Gauta - x {x} ir  - y {y} ")

if  x<y:
     print('y yra didesnis uz x')

elif  y<x:
     print('x yra didesnis uz y')

else:
    print( ' x ir y lygus')




x = random.randint(5 , 50)
print(f" Gauta - x {x} euru ")

if x >= 2:
    print('batai.....')
    x-=2 # minusuja is sumos ( siuo atveju x )
if x >= 4:
    print('kojines.....')
    x -= 4  # minusuja is sumos ( siuo atveju x )
if x >= 1:
    print('batraisciai.....')
    x -= 1  # sitas if ir elif kartu su else jau bus kaip vienas blokas
elif x >=4:
    print('kamuolys')
    x-=4
elif x >=2:
    print('lazda')
    x-=2
else:
    print('Pabaiga')

print(x)


print()
a = 200
b = 300

print("A") if a < b else print("B")


print("A") if a > b else print("=") if a==b else print("B")




print()

mlb = ("yankees", "red sox", "pirates", "white sox", "merlins")

for x in mlb:

    if x == "white sox":
        print(x.upper())

    if x == "red sox":
        print(x.title())

    else:
        print(None)