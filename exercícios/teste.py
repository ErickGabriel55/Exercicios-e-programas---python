lista1 = ['a', 'b']
lista2 = ['c', 'd']
lista3 = []
lista4 = lista3.append(lista1)
lista5 = lista3.append(lista2)
lista6 = lista1 + lista2
lista7 = [lista1, lista2]
print(f'antes do extend em lista 6 {lista6}')
lista6.extend(lista1)
lista6.extend(lista2)
print(lista3, lista4, lista5, lista6, lista7)
l = []
print(l)
l += [1]
print(l)
l.append(3)
print(l)
l.extend(['c'])
print(l)