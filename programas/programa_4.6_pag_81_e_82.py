while True:
    categoria = int(input('Digite a categoria do produto (de 1 a 5): '))
    if 1 <= categoria <= 5:
        if categoria == 1:
            preço = 10
        else:
            if categoria == 2:
                preço = 18
            else:
                if categoria == 3:
                    preço = 23
                else:
                    if categoria == 4:
                        preço = 26
                    else:
                        if categoria == 5:
                            preço = 31

        print(f'O preço do produto é: R${preço:6.2f}')
        break
    else:
        print('Categoria inválida digite um número de 1 a 5!')