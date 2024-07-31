#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total ganho com juros no período.
#Usando o while, contador e acumulador
#Altere o programa anterior de forma a perguntar também o valor depositaddo mensalmente.
#Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
#Já com a alteração!
#Pergunta quanto já está na conta
deposito = float(input('Qual o valor do deposito? R$'))
#pergunta a taxa de juros da conta poupança
taxa_juros = float(input('Qual a taxa de juros em porcentagem: '))
#Pergunta o quanto será depositado a cada mes
deposito_mes = float(input('Qual o valor que será depositado mensalmente? R$'))
#variáveis necessárias
saldo = deposito
#contador que estudei no livro
meses = 1
#acumulador que estudei no livro
ganho = 0
#loop com os calculos e etc
while meses <= 24:
    rendimento_mes = saldo * (taxa_juros / 100 / 12)
    saldo += rendimento_mes + deposito_mes
    ganho += rendimento_mes
    print(f'O depósito foi de R${deposito_mes}.\n Teve um rendimento no mês {meses} de R${rendimento_mes:.2f} e saldo é de {saldo:.2f}!')
    meses += 1
print(f'O total de juros ganho no período foi de R${ganho:.2f}!')