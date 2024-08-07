soma = 0
conta = 0
while True:
    numeron = int(input('Digite um numero ou 0 pra sair: '))
    if numeron == 0:
        break
    conta += 1
    soma += numeron
    media = soma // conta
print(f'Você digitou {conta} números!\nA soma desses números {soma}!\nA média desses números é {media}!')