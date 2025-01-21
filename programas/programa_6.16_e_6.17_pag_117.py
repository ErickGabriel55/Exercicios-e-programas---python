"""6.16 - Listas com elementos de tipos diferentes e 6.17 - Listas de listas e 6.18 - Impressão de compras"""

produto1 = ["maçã", 10, 0.30]
produto2 = ["pera", 5, 0.75]
produto3 = ["kiwi", 4, 0.98]
compras = [produto1, produto2, produto3]
print(compras[1][1])
# Acredito que seja matriz em python, apesar de que o livro não menciona essa estrutura de dados
for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]:5.2f}")

