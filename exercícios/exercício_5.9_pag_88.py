penis: int = int(input('Qual número quer dividir? '))
cu: int = int(input(f'Quer dividir {penis} por quanto? '))
original = penis
print(original)
priquito = 0
while penis > 0:
    penis2 = penis - cu
    print(penis2)
    priquito = priquito + 1
    penis = penis2

print(f'O resultado de {original} dividido por {cu} é igual {priquito}')
print(f'O número {original} foi subtraído por {cu}, {priquito} vezes!')