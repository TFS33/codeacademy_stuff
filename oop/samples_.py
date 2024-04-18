data = [1, 2, 3]

# python magic methods pasiziureti dunder methods

class Animal(object): # object nebutinas klase irankis sukurti objekta
   def __int__(self, age: int = 10, name = 'Pearch', *args, **kwargs): #self #reiskia pati klase init konstruktorius
        self.name = 'Pearch'
        self.age = 10
        self.age_after_ten_years = self.age + 10    #atributai
   # pass


#a = Animal

#print(a, a())

#print(a.mro())

animal = Animal()# skliaustai is a must
print(animal.age, animal.name)

animal.age = 15

print(animal.age, animal.age)