# Simulação de uma fila de banco
ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print(f'Digite A para adicionar um cliente ao fim da fila.\nDigite R para realizar o atendimento.\nS para sair')
    operacao = input('Operação (A, R ou S): ').upper()
    operacaol = list(operacao)
    while len(operacaol) >= 0:
        if operacaol[0] == 'R':
            if len(fila) > 0:
                atendido = fila.pop(0)
                operacaol2 = operacaol.pop(0)
                print(f'Cliente {atendido} atendido')
            else:
                print('Não existem clientes na fila!')
        elif operacaol[0] == 'A':
            ultimo += 1
            operacaol2 = operacaol.pop(0)
            fila.append(ultimo)
        elif operacaol[0] == 'S':
            break
        else:
            print('Operação inválida! Por favor, digite novamente dentre as opções A, R ou S!')


# CÓDIGO DO PROFESSOR (TA BEM MELHOR ): )
# último = 10
# fila = list(range(1, último + 1))
#while True:
#    print(f"\nExistem {len(fila)} clientes na fila")
#    print("Fila atual:", fila)
#    print("Digite F para adicionar um cliente ao fim da fila,")
#   print("ou A para realizar o atendimento. S para sair.")
#    operação = input("Operação (F, A ou S):")
#    x = 0
#    sair = False
#    while x < len(operação):
#        if operação[x] == "A":
#            if len(fila) > 0:
#               atendido = fila.pop(0)
#                print(f"Cliente {atendido} atendido")
#            else:
#                print("Fila vazia! Ninguém para atender.")
#        elif operação[x] == "F":
#            último += 1  # Incrementa o ticket do novo cliente
#           fila.append(último)
#        elif operação[x] == "S":
#           sair = True
#            break
#        else:
#            print(
#                f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!"
#           )
#        x = x + 1
#    if sair:
#        break
