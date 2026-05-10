nome=str(input("Qual o nome do jogador? "))
quantidade=int(input("Qual a quantidade de partidas? "))
lista=[]
total=0
dic2={}
for c in range(1,quantidade+1):
    goln=int(input('Quantos gols na {}a partida? '.format(c)))
    lista.append(goln)
    total=total+goln
    dic2[c]=goln
print('-=-'*30)
dic={'Nome':nome,'Gols':lista,'Total':total}
for chave,valor in dic.items():
    print('O campo {} tem o valor {}'.format(chave,valor))
print('-=-'*30)
print('O jogador {} jogou {} partidas.'.format(nome,quantidade))

for chave,valor in dic2.items():
    print('     => Na partida {}, fez {} gols'.format(chave,valor))
print('Foi um total de {} gols'.format(total))
