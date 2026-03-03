cont=0
ordem=[]
resposta='S'

while resposta=='S':
    num=int(input('Digite um numero inteiro qualquer: '))
    ordem.append(num)
    cont=cont+1
    resposta=str(input('Quer continuar? [S/N] ').upper())
print('a) Foram digitados {} numeros'.format(cont))
ordem2=sorted(ordem,reverse=True)
print('b) A ordem na descrescente: ',ordem2)
pos=ordem.count(5)
if pos==0:
    print('c) Nao ha "5" na lista.')
else:
    print('c) Ha {} 5`s na lista.'.format(pos))
