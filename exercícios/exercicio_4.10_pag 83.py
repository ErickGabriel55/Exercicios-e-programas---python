#pergunta quantos kwh a pessoa consumiu
kwh = float(input('Quantos \033[0;31mKWH\033[m vc \033[1;31mconsumiu\033[m? '))
#pergunta o tipo de instalação
instalacao = str(input('Qual o tipo de instalação (R para residencial, I para insdústrias, C para comércios)? ')).upper()
#variáveis e condições para os cálculos
if kwh >= 500 and (instalacao == 'R' or instalacao =='RESIDENCIAL'):
    pagamento = kwh * 0.40
elif kwh < 500 and (instalacao == 'R' or instalacao =='RESIDENCIAL'):
    pagamento = kwh * 0.65
elif kwh >= 1000 and (instalacao == 'C' or instalacao =='COMÉRCIOS' or instalacao =='COMERCIOS' or instalacao =='COMERCIAL'):
    pagamento = kwh * 0.55
elif kwh < 1000 and (instalacao == 'C' or instalacao =='COMÉRCIOS' or instalacao =='COMERCIOS' or instalacao =='COMERCIAL'):
    pagamento = kwh * 0.60
elif kwh >= 5000 and (instalacao == 'I' or instalacao =='INDUSTRIAS' or instalacao =='INDÚSTRIAS'):
    pagamento = kwh * 0.55
else:
    print("Tipo de instalação não reconhecido.")
    pagamento = 0
print(f'O valor total a pagar será de R${pagamento}!')