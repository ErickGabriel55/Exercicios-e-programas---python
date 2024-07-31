lista1 = []
lista2 = []
juncao_lista = []
divisor = ('-' * 100)
while True:
    lista_usuario1 = input('Digite algo para adicionar a primeira lista. Digite sair quando terminar: ')
    if lista_usuario1.lower() == 'sair':
        break
    lista1.append(lista_usuario1)
print(divisor)
while True:
    lista_usuario2 = input('Digite algo para adicionar a segunda lista. Digite sair quando terminar: ')
    if lista_usuario2.lower() == 'sair':
        break
    lista2.append(lista_usuario2)
print(divisor)
juncao_lista = lista1 + lista2
print(f'A sua primeira lista foi {lista1}. \nA sua segunda lista foi {lista2}. \nA junção das duas resultou em {juncao_lista}.')


""" código do professor
primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if e == 0:
        break
    primeira.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if e == 0:
        break
    segunda.append(e)
terceira = primeira[:]  # Copia os elementos da primeira lista
terceira.extend(segunda)
x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x = x + 1
"""
