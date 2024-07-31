# Simulação de uma fila de banco
ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print(f'Digite A para adicionar um cliente ao fim da fila.\nDigite R para realizar o atendimento.\nS para sair')
    operacao = input('Operação (A, R ou S): ').upper()
    if operacao == 'R':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} antendido!')
        else:
            print('não há clientes na fila')
    elif operacao == 'A':
        ultimo += 1  # incrementa o ticket do cliente
        fila.append(ultimo)
    elif operacao == 'S':
        break
    else:
        print('Operação inválida, digite novamente!')
