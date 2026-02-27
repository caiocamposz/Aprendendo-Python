lista1=[]
lista2=[]

num=int(input('Digite um valor inteiro: '))
lista1.append(num)
resposta=str(input('Voce deseja continuar? [S/N] ')).upper()
while resposta=='S':
    num2=int(input('Digite outro valor inteiro: '))
    while num2 in lista1:
        num2 = int(input('Digite outro valor inteiro, pois esse ja esta na lista: '))
    if num2 not in lista1:
        lista1.append(num2)
    resposta = str(input('Voce deseja continuar? [S/N] ')).upper()
    #**** AQUI ****
else:

    while lista1 !=[]: # Daria para usar lista3=list(lista1) em (*) e depois print(sorted(lista3)) que ja colocaria automaticamente em ordem crescente.
        minimo=min(lista1)
        lista2.append(minimo)
        lista1.remove(min(lista1))
    tup2=tuple(lista2)
    print(tup2)








