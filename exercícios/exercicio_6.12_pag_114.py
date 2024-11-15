L =  [1, 7, 2, 4]
minimo = L[0]
maximo = L[0]
for e in L:
    if e > maximo:
        maximo = e
    elif e < maximo:
        maximo = minimo
print(maximo, minimo)
