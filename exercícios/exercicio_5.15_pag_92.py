# Escreva um programa para controlar uma pequena máquina registradora,
# Você deve solicitar ao usuário que digite o código do produto
# e a quantidade comprada.
# Utilize a tabela de códigos a seguir para obter o preço de cada produto:
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro "Código inválido”.

# Exibe a tabela de preços e o código do produto para o usuário
print('Código       Preço\n'
      '   1         0,50\n'
      '   2         1,00\n'
      '   3         4,00\n' 
      '   5         7,00\n'
      '   9         8,00')
print('O produto será adicionado ao seu carrinho!\nSerá exibido o total comprado ao fim das compras!!')

# Variável pra guardar o total de compras
total = 0

# inicia o loop com
while True:
    # Pergunta quanto o usuário irá comprar e encerra o programa caso seja 0
    quantidade_produto = int(input('Você irá comprar quantos produtos ou 0 para sair? '))
    if quantidade_produto == 0:
        break
    # Pergunta o código do produto
    produto = int(input('Qual o código do produto? '))
    # Condição para cada produto
    if produto == 1:
        preco = 0.50
    elif produto == 2:
        preco = 1.00
    elif produto == 3:
        preco = 4.00
    elif produto == 5:
        preco = 7.00
    elif produto == 9:
        preco = 8.00
    else:
        # Caso não seja nenhum dos códigos da tabela ou 0 exibe uma mensagem de erro
        print('Código inválido!')
        continue
    # Variável que guardou totoal em R$ das compras
    total += preco * quantidade_produto

# exibe o total das compras em R$
print(f'O total de compras foi de R${total:.2f}')
