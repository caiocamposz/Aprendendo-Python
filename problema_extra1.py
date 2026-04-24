Determine, para um número inteiro positivo n, a página, a letra (de A a Z) e a posição correspondente em uma sequência em que cada letra aparece um número de vezes igual à sua ordem no alfabeto (por exemplo, A suporta 1 ocorrência, D suporta 4 ocorrências).
Solucao que pensei:
num=int(input('Digite um numero inteiro positivo: '))
while num<1:
    num=int(input('Tente novamente. Digite um numero inteiro valido ( >0) : '))
alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pagina=num//351
if num%351==0:
    print('Pagina: {}, Letra: Z, Posicao: 26'.format(pagina))
else:

    resto=num-(pagina*351)

    delta=(1+8*resto)**(1/2)
    equacao=(-1+delta)/2


    for c in range(0,26):
        if equacao>c and equacao<=c+1:
            letra=alfabeto[c]
            valor=int(equacao)
            pos2=c+1


    posicao=resto-(valor*(valor+1)/2)
    if posicao==0:
        posicao=pos2


    print('Pagina: {}, Letra: {}, Posicao: {}'.format(pagina+1,letra,int(posicao)))
