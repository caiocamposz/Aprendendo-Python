import random
contador=0
lista=(1,2,3,4,5,6,7,8,9,10)
num=int(input('Escolha seu numero: '))
while num<0:
    num=int(input('Escolha corretamente seu numero: '))
lado=input('Escolha seu lado ( PAR /IMPAR ): ').upper()
while lado!='PAR' and lado!='IMPAR':
    lado=input('Escolha seu lado de forma correta ( PAR/IMPAR ): ').upper()
escolha=random.choice(lista)
soma=num+escolha
resto=soma%2
if resto==1:
    resultado = 'IMPAR'
elif resto==0:
    resultado = 'PAR'
while (resto==1 and lado=='IMPAR' )or (resto==0 and lado=='PAR'):
    print('Voce venceu, pois {} + {} = {} que eh um numero {}'.format(num,escolha,soma,resultado))
    contador=contador+1
    num=int(input('Escolha seu numero: '))
    while num < 0:
        num = int(input('Escolha corretamente seu numero: '))

    lado = input('Escolha sua lado ( PAR /IMPAR ): ').upper()
    while lado != 'PAR' and lado != 'IMPAR':
        lado = input('Escolha seu lado de forma correta ( PAR/IMPAR ): ').upper()
    escolha = random.choice(lista)
    soma = num + escolha
    resto = soma % 2
    if resto == 1:
        resultado = 'IMPAR'
    elif resto == 0:
        resultado = 'PAR'
if (resto==1 and lado=='PAR' )or (resto==0 and lado=='IMPAR'):
    print('Voce perdeu, pois escolheu um numero {} e {} + {} = {} que  eh um numero {}.Com isso o nosso jogo acabou, voce venceu um total de {} jogos.'.format(lado,num,escolha,soma,resultado,contador))



