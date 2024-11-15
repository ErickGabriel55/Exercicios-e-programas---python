'''Não podemos substituir o while True por for, pois não sabemos quantas vezes o usuário irá executar as operações'''

último = 0
fila1 = []
fila2 = []
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} na fila 2.")
    print("Fila 1 atual:", fila1)
    print("Fila 2 autal:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
    print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
    print("S para sair.")
    operação = input("Operação (F, G, A, B ou S):")
    x = 0
    sair = False
    for l in operação:
        # Aqui vamos usar fila como referência a fila 1
        # ou a fila 2, dependendo da operação.
        if l == "A" or l == "F":
            fila = fila1
        else:
            fila = fila2
        if l == "A" or l == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif l == "F" or l == "G":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif l == "S":
            sair = True
            break
        else:
            print(
                f"Operação inválida: {l} na posição {x}! Digite apenas F, A ou S!"
            )
        x = x + 1
    if sair:
        break