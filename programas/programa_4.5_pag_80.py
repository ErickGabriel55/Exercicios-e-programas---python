minutos = int(input('Quantos minutos você utilizou esse mês: '))
if minutos < 200:
    preco = 0.18
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print(f'Você vai pagar este mês: R$ {minutos * preco:6.2f}')