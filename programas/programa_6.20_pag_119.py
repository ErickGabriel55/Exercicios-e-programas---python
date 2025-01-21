# Ordenação pelo metodo de bolhas (bublesort)
l = [1, 2, 3, 4, 5] # criação de uma lista
fim = 5 # acredito que seja quantas vezes acontecerá o bublesort, de acordo com o tamanho da lista
while fim > 1:  # enquanto o fim for maior que um
    print("-" * 8)
    trocou = False # inicializa
    x = 0 # inicializa um contador
    while x < (fim - 1): # enquanto x for menor que 4
        if l[x] < l[x + 1]: # se o numero atual for maior que o posterior
            trocou = True # a variável inicializada anteriormente recebe verdadeiro
            temp = l[x] # não entendi
            l[x] = l[x + 1] # não entendi
            l[x + 1] = temp # não entendi
        x +=1 # incrementa o contador em 1
    if not trocou:
        break
    fim -= 1
    for e in l:
        print(e)