# utilização de filas com duas listas ou duas filas
último = 10
fila = list(range(1, último + 1))
ultimo2 = 15
fila2 = list(range(1, ultimo2 + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na primeira fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da primeira fila,")
    print("ou A para realizar o atendimento. \nS para sair.")
    operação = input("Operação (F, A ou S): ").upper()
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Não há clientes na fila.")
        elif operação[x] == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "S":
             sair = True
             break
        else:
            print(
                f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!")
        x = x + 1
    if sair:
        break
while True:
    print(f"\nExistem {len(fila2)} clientes na segunda fila")
    print(f"A segunda fila atualmente: {fila2}")
    print("Digite G para adicionar um cliente ao fim da segunda fila,")
    print("ou B para realizar o atendimento. \nS para sair.")
    operação2 = input("Operação (G, B ou S): ").upper()
    sair2 = False
    x = 0
    while x < len(operação2):
        if operação2[x] == 'B':
            if len(fila2) > 0:
                atendido2 = fila2.pop(0)       
                print(f"Cliente {atendido2} atendido")
            else:
                print('Não existem clientes na segunda fila!')
        elif operação2[x] == 'G':
            ultimo2 += 1
            fila2.append(ultimo2)
        elif operação2[x] == 'S':
            sair2 = True
            break
        else:
            print('Operção inválida digite apenas B, G, S para editar a segunda fila!')
        x += 1
    if sair2:
        break

# CÓDIGO DO PROFESSOR
#último = 0
#fila1 = []
#fila2 = []
#while True:
#    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} na fila 2.")
#    print("Fila 1 atual:", fila1)
#    print("Fila 2 autal:", fila2)
#    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
#    print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
#    print("S para sair.")
#    operação = input("Operação (F, G, A, B ou S):")
#    x = 0
#    sair = False
#    while x < len(operação):
#         Aqui vamos usar fila como referência a fila 1
#         ou a fila 2, dependendo da operação.
#        if operação[x] == "A" or operação[x] == "F":
#            fila = fila1
#        else:
#            fila = fila2
#        if operação[x] == "A" or operação[x] == "B":
#            if len(fila) > 0:
#                atendido = fila.pop(0)
#                print(f"Cliente {atendido} atendido")
#            else:
#                print("Fila vazia! Ninguém para atender.")
#        elif operação[x] == "F" or operação[x] == "G":
#            último += 1  # Incrementa o ticket do novo cliente
#            fila.append(último)
#        elif operação[x] == "S":
#            sair = True
#            break
#        else:
#            print(
#                f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!"
#            )
#        x = x + 1
#    if sair:
#        break#