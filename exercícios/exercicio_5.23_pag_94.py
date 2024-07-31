numero = int(input('Digite um número: '))
contador = 1
total = 0
while contador <= numero:
    if numero % contador == 0:
        print('\033[0:36m', contador, end=' ')
        total += 1
    else:
        print('\033[0:31m', contador, end=' ')
    contador += 1
print(f'\n\033[mO número \033[0:32m{numero} \033[mfoi divisível \033[0:36m{total} \033[mvezes!')
if total == 2:
    print('\033[0:36mE é um número primo!')
else:
    print('\033[0:31mE não é um número primo!')
