#valor da casa
casa = float(input('Qual o valor da casa que será comprada? R$'))
#qual o salário da pessoa?
salario = float(input('Qual o seu salário? R$'))
#pra pagar em quantos anos?
quantas_parcelas = float(input('Vai pagar em quantos anos? '))
#quantidade de anos em meses
meses_pagar = 12 * quantas_parcelas
#prestação da casa por mês
prestacao_mensal = casa / meses_pagar
#condição pra cada situação
if prestacao_mensal <= salario * 0.30:
    print(f'O valor mensal da casa a pagar será de R${prestacao_mensal:.2f} por mês!')
else:
    print('Infelizmente não será possível que vc compre a casa ;-;. \nProcure preços menores ou aumente a quantidade de anos a pagar, obrigado!')