# Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys.
# Reikšmę galite saugoti kintamajame.
# Tada sukurkite ciklą, einantį per visas galimas kombinacijas, kol rasite tą, kurią įvedėte.

import random
from random import randint



pin = 4587

bruteforce = random.randint(0000, 9999)

while True:
    if bruteforce == pin:
        print('NULAUZTA')
    break
else:
    print('Wrong PIN')




# for i in range(4):
   # result += str(randint(0, 10))