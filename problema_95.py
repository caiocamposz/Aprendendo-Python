resposta='S'
lista=[]
while resposta=='S':
    print('-' * 50)
    dic={}
    lista_gol=[]
    total = 0
    dic['nome'] = str(input("Qual o nome do jogador? ")).capitalize()
    dic['quantidade'] = int(input("Qual a quantidade de partidas? "))
    for c in range(1, dic['quantidade'] + 1):
        goln = int(input('Quantos gols na {}a partida? '.format(c)))
        lista_gol.append(goln)
        total = total + goln
    dic['total'] = total
    dic['gols'] = lista_gol
    lista.append(dic)
    resposta=str(input("Quer continuar [S/N]: ")).upper()
print('-='*50)
print('cod  nome                          total  gols')
espacos=28
print('-'*70)
for c in range(0,len(lista)):
    print(' {}  {}{}    {}     {}'.format(c, lista[c]['nome'],(' '*(28-len(lista[c]['nome']))),lista[c]['total'], lista[c]['gols']))

jogador = int(input('Quer mostrar mais informacoes de qual jogador (999 para parar)? '))
print('-' * 70)


while jogador !=999:
    if jogador in range(0,len(lista)):
        print('Levantamento do jogador: {}'.format(lista[jogador]['nome']))
        for c in range(0,len(lista[jogador]['gols'])):
            print('   => No jogo {} fez {} gols'.format(c+1, lista[jogador]['gols'][c]))
        print('Sendo assim, fez {} gols no total.'.format(lista[jogador]['total']))
        print('-' * 70)
        jogador = int(input('Quer mostrar mais informacoes de qual jogador (999 para parar)? '))
    else:
        print('Codigo invalido, tente novamente.')
        jogador = int(input('Quer mostrar mais informacoes de qual jogador (999 para parar)? '))

else:
    print('Finalizando!')



