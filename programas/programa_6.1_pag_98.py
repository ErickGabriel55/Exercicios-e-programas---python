# Cálculo de média
notas = [6, 7, 5, 8, 9]  # Criamos a lista [] de notas
soma = 0
x = 1
while x < 5:   # Criamos a estrutura de repetição para variar enquanto este for menor que 5
    soma += notas[x]
    x += 1
print(f'Média: {soma / x:5.2f}')
