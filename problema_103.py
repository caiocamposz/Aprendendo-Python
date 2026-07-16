def ficha(nome='<desconhecido>',gol=0):
    nome_1=nome
    gol_1=gol

    if nome_1 == '' and gol == '':
        nome_1='<desconhecido>'
        gol_1=0

    elif nome_1=='':
        nome_1='<desconhecido>'
    elif gol=='':
        gol_1=0
    print(f'O jogador {nome_1} fez {gol_1} gol(s) no campeonato.')

nome_2=str(input('Digite o nome do jogador: ').strip())
gol_2=str(input('Digite o numero de gols: ').strip())
if gol_2.isnumeric()==True:
    gol_2=int(gol_2)
else:
    gol_2=0

ficha(nome_2,gol_2)

