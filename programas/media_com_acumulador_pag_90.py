x = 1
soma = 0
while x <= 5:
    n = int(input(f'{x} Digite o número: '))
    soma += n
    x += 1
resultado = soma / 5
print(f'Média: {resultado:.1f}')
