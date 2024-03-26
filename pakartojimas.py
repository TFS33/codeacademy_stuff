var = (1.0, 2.0, 3.0, 4.0)
var2 = (1, 2, 3, 4)

print(var, var2)

var = list(var)
var2 = list(var2)


print(varlist, varlist2)

varlist01 = (sum(varlist))
varlist02 = (sum(varlist2)/ len(varlist2))

print(varlist01, varlist02)

# Tomas4. Pirmo list sumą daliname iš 2 ir antro listo istraukti dalm


varlist011 = varlist01 / 2
varlist021 = varlist02 ** 2

print(int(varlist011), int(varlist021))

varlist_lyg = varlist01 == varlist02
varlist_nel = varlist011 != varlist021

print(varlist_lyg, varlist_nel)

varlist_bule = not varlist_lyg and varlist_nel

print(varlist_bule)

