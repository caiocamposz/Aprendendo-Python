import random
lista1=[]
def sorteia(lista):
    for c in range(0,5):
        num=random.randint(1,10)
        lista.append(num)
    print('Sua lista:' ,lista)


def soma_par(lista):
    soma=0
    for num in lista:
        if num%2==0:
            soma=soma+num
    print('A soma dos números pares da lista:', soma)

sorteia(lista1)
print('                                            ')
soma_par(lista1)

