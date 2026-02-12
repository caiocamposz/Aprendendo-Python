print('Seja bem vindo a loja!')
lista= ['SIM','S','N','NAO']
listaS=['SIM','S']
listaN=['NAO','N']
resposta= 'SIM'
cont2=0
soma=0
mais_barato=''
contador=0
valor_barato=None



while resposta in listaS:
    nome=str(input('Digite o nome do produto: '))
    preco=int(input('Digite o valor do produto: '))
    if contador==0:
        valor_barato=preco
        mais_barato=nome
    else:
        if valor_barato>preco:
            mais_barato=nome
            valor_barato=preco
    contador=contador+1
    soma=soma+preco
    if preco>1000:
        cont2=cont2+1
    resposta=str(input('Deseja continuar? [S/N] ')).strip().upper()
else:
    print('Terminamos. O total das compras foi de {}, com {} custando mais de 1000 reais e o {} eh o produto mais barato .'.format(soma,cont2,mais_barato))


