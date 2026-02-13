tupla=[]
cont9=0
tuplaPAR=[]

for c in range(1,5):
    num=int(input("Digite um numero inteiro positivo:"))
    while num<0:
        num=int(input("Digite corretamente um numero inteiro:"))
    tupla.append(num)
    if num==9:
        cont9=cont9+1
    if num%2==0:
        tuplaPAR.append(num)
tupla111=tuple(tupla)
print('a) O 9 apareceu {} vezes'.format(cont9))
if 3 in tupla111:
    print('b) O primeiro 3 aparece na tupla na posicao', tupla111.index(3)+1)
print('c) Os numeros pares sao:', *tuplaPAR)
