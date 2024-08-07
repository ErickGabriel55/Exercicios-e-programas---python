l = [15, 7, 27, 39,]
p = int(input("Digite o valor a procurar: "))
x = 0
while x < len(l):
    if l[x] == p:
        break
    x += 1
if x < len(l):
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado')