Problema_extra2 (inverso do problema_extra1): Dada uma letra (de A a Z) e uma posição válida associada a ela, determine o número inteiro n correspondente na sequência descrita anteriormente.

alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
letra_al=random.choice(alfabeto)

teste1=alfabeto.find(letra_al)
n1=int(teste1+1)
n2=n1-1
soma_ant=n2*(n2+1)/2
pos_al=random.randint(1,n1)
num=soma_ant+pos_al

print('O numero sabendo que se encontra na letra e posicao: {} ; {}'.format(letra_al,pos_al))
print('Logo, o numero eh ',int(num))
