import random
lista=[]
numero=int(input('Digite a quantidade de jogos da MegaSena que voce deseja: '))
for c in range(1,numero+1):
    for d in range(1,7):
        escolhido=random.randint(1,60)
        while escolhido in lista:
            escolhido=random.randint(1,60)
        lista.append(escolhido)
    print('Jogo {}: {}'.format(c, sorted(lista)))
    lista = []


