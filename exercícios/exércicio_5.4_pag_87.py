fim = int(input('Digite o valor último número a imprimir: '))
x = 1
while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x + 1