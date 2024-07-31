pontos  = 0
questoes = 1
while questoes <= 3:
    resposta = input(f'Resposta da questão {questoes}: ').lower()
    if questoes == 1 and resposta == 'b':
        pontos = pontos + 1
    elif questoes == 2 and resposta == 'a':
        pontos = pontos + 1
    elif questoes == 3 and resposta == 'd':
          pontos = pontos + 1
    questoes = questoes + 1
print(f'O aluno fez {pontos} ponto(s)!')
