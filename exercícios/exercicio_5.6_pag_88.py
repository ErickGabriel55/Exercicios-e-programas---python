tabuada: int = int(input('Tabuada de qual número? '))
x = 0
resultado =  tabuada * x
while x <= 10:
    print(f'{tabuada} x {x} = {resultado}')
    x = x + 1
    resultado =  tabuada * x