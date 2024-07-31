expressão = str(input("Digite os parenteses para a verificação. "))
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] != "(" and expressão[x] != ")":
        print("Por favor, digite apenas parenteses para que a verificação possa ser realizada!\nENCERRANDO PROGRAMA!")
        break
    if expressão[x] == "(":
        pilha.append("(")
    elif expressão[x] == ")":
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            pilha.append(")") 
            break
    x += 1
if len(pilha) == 0:
    print("Verificação concluida!\nOS PARENTESES FORAM ABBERTOS E FECHADOS CORRETAMENTE!")
else:
    print("Verificação concluida!\nOS PARENTESES --->NÂO<--- FORAM ABBERTOS E FECHADOS CORRETAMENTE!")
