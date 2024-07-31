fim = int(input('Qual o ultimo número a ser mostrado? '))
x = 1
while x <= fim:
    if x % 3 == 0:
        print(x)
    x = x + 1