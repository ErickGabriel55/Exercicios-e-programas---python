# Controle de utilização de salas de um cinema
lugaresVazios = [10, 2, 1, 3, 0]
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lugaresVazios) or sala < 1:
        print("Sala inválida")
    elif lugaresVazios[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lugaresVazios[sala - 1]} vagos):"))
        if lugares > lugaresVazios[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número invalido!")
        else:
            lugaresVazios[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
print("Utilização das salas")
for x, l in enumerate(lugaresVazios):
    print(f"Sala {x + 1} - {l} lugar(es) vazios(s)")

