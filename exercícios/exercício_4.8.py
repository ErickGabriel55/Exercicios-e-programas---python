#pergunta os números
numero1 = int(input('Qual o primeiro número: '))
numero2 = int(input('Qual o segundo numero: '))
#repetição
while True:
        # pergunta qual a operação que irá ser realizada
        operacao = str(input('Qual a operação a ser realizada (+, -, x, /): '))
        # condição para cada operação
        if operacao == '+':
            resultado = numero1 + numero2
            break
        else:
            if operacao == '-':
                resultado = numero1 - numero2
                break
            else:
                if operacao == 'x' or operacao == '*' or operacao == '.':
                    resultado = numero1 * numero2
                    break
                else:
                    if operacao == '/':
                        resultado = numero1 / numero2
                        break
                    else:
                        print('Por favor, digite uma operação válida!')
print(f'O resultado é: {resultado}')