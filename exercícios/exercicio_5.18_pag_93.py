# contagem de cédulas

valor = float(input('Digite o valor a pagar:  '))
cedulas = 0
atual = 100
apagar = int(valor * 100)
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédulas de R${atual / 100:.2f}')
        if apagar == 0:
            break

        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        if atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cedulas = 0