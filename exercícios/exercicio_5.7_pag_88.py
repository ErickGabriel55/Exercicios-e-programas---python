tabuada: int = int(input('Tabuada de qual número? '))
x: int = int(input('Qual será o fim da tabuada? '))
contador: int = 0
while contador <= x:
    resultado = tabuada * contador
    print(f'{tabuada} x {x} = {resultado}')
    contador = contador + 1