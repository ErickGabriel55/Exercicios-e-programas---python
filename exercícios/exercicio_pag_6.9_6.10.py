# Exercício 06-09: Procurando dois valores
# Exercício 06-10: Procurando dois valores e exibindo a posição onde foram encontrados


l = [15, 7, 27, 39,]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))
x = 0
y = 0


while x < len(l):
    if l[x] == p:
        break
    x += 1
if x < len(l):
    print(f'{p} achado na posição {x}')
else:
    print(f'O {p} não foi encontrado!')


while y < len(l):
    if l[y] == v:
        break
    y += 1
if y < len(l):
    print(f"O {v} achado na posição {y}")
else:
    print(f'O {v} não foi encontrado!')



if x < y:
    print(f"O {p} foi achado primeiro!")

elif y < x:
    print(f"O {v} foi achado primeiro!")

elif y == x:
    print("Os números são iguais!")
