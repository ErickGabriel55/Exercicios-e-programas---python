tabuada: int = int(input("Qual o primeiro número? "))
x: int = int(input("Qual  o segundo número? "))
contador = 0
resultado = 0

while contador < x:
    resultado = resultado + tabuada
    contador = contador + 1

print(f"O seu resultado é {resultado}")
