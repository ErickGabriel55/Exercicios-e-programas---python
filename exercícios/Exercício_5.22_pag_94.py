# fazer a lista com as opções
# fazer a tabuada de operações
# comt repetições aninhadas (while)

while True:
    print('              Escolha uma opção: ')
    print('''              1- Subtração
              2- Adição
              3- Multiplicação
              4- Divisão
              5- Sair''')
    print('-' * 44)
    operacao = int(input('Escolha um dos números das opções acima: '))

    if operacao == 5:
        print('O programa foi finalizado!')
        break
    elif operacao > 5:
        print('Digite novamente')
    elif operacao >= 1 and operacao < 5:
        numero = int(input('Qual o numero deseja ver a tabuada? '))
        print('-' * 44)
        tabuada = numero
        contador = 1

        while contador <= 10:
            if operacao == 1:
                print(f'{tabuada} - {contador} = {tabuada - contador}')
            elif operacao == 2:
                print(f'{tabuada} + {contador} = {tabuada + contador}')
            elif operacao == 3:
                print(f'{tabuada} x {contador} = {tabuada * contador}')
            elif operacao == 4:
                print(f'{tabuada} ÷ {contador} = {tabuada / contador:.2f}')
            contador += 1