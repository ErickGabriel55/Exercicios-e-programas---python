# Adição de elementos a lista
lista = []
while True:
    numero = int(input('Digite o número que vc quer adicionar ou 0 para sair: '))
    if numero == 0:
        break
    lista.append(numero)
x = 0
while x < len(lista):
    print(lista[x], end=" ")
    x += 1
