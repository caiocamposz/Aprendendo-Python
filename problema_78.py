lista1=[]


num=int(input('Digite o numero para a posição 1: '))
lista1.append(num)
maior=num
menor=num
pos=pos2=1
for c in range(1,5):
    num=int(input('Digite o numero para a posição {}: '.format(c+1)))
    lista1.append(num)
    if num>maior:
        maior=num
        pos=c+1
    if num<menor:
        menor=num
        pos2=c+1

tup1=tuple(lista1)
print('Voce digitou os seguintes valores: ',tup1)
print('O maior valor eh {} e esta na posicao {}'.format(maior,pos))
print('O menor valor eh {} e esta na posicao {}'.format(menor,pos2))



