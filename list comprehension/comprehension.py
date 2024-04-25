squares = []
for number in range(10):
    squares.append(number * number)
print(squares)


squares = [number * number for number in range(10)]
print(squares)


names = ["Albert", "Alma", "Joseph", "Zoro"]
print([name for name in names if name.startswith("A")])


funcija = '5 + 8 + 9'
print(funcija)
print(eval(funcija))