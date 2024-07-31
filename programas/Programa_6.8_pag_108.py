prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos naa pilha")
    print(f"Pilha atua: {pilha}")
    print("Digite E para empilhar um novo prato")
    print("Ou D para desempilhar. S para sair.")
    operacao = input("Qual operação deseja realizar na pilha (E, D ,S)? ").upper()
    if operacao == 'D':
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"prato {lavado} lavado")
        else:
            print("Pilha vazia nenhum prato a ser lavado!")
    elif operacao == 'E':
        prato += 1
        pilha.append(prato)
    elif operacao == 'S':
        break
    else:
        print("Operação inválida digite apenas E, D, S.")