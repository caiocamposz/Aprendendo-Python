
ordem=[]
resposta='S'
lista_par=[]
lista_impar=[]
while resposta=='S':
    num=int(input('Digite um numero inteiro qualquer: '))
    ordem.append(num)
    paridade=num%2
    if paridade==0:
        lista_par.append(num)
    elif paridade==1:
        lista_impar.append(num)
    resposta=str(input('Quer continuar? [S/N] ').upper())
print('A lista geral: {}'.format(ordem))
print('A lista dos numeros impares: {}'.format(lista_impar))
print('A lista dos numeros pares: {}'.format(lista_par))

