tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Feijão":1.50}
print(f'Tomate antes de modificar: {tabela["Tomate"]}')
print(f'Primeira vez: {tabela}')
tabela["Tomate"] = 2.50
tabela["Cebola"] = 1.20
print(f'Segunda vez: {tabela}')
print("manga" in tabela)
print("Batata" in tabela)
print(tabela.keys())
print(tabela.values())

