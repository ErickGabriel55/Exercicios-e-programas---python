# Repetição com len()
from time import sleep

lista = [1, 2, 3]
x = 0
lista.append('b')
for lista2 in range(len(lista)):
# while x < len(lista):
    print(lista[x])
    x += 1
    sleep(1)
