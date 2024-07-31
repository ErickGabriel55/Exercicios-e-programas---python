notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
contador = 1
while contador < 7:
    notas[contador] = float(input(f'Digite a nota {contador}: '))
    soma += notas[contador]
    contador += 1
contador = 1
while contador < 7:
    print(f'Nota {contador}: {notas[contador]:6.2f}')
    contador += 1
media = soma / contador
print(f'A sua média foi: {media:6.2f}')
