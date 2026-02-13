lista=[]
tupla=()
contador=0
resposta='S'
while resposta=='S':
    nome=str(input('Produto: '))
    while nome=='':
        nome=str(input('Digite o nome do produto: '))
    preco1 = str(input('Preco: '))
    while not preco1.isdigit():
        preco1=str(input('Digite o preco: '))
    preco=int(preco1)
    lista.append(nome)
    lista.append(preco)
    tupla=tuple(lista)
    contador=contador+1

    resposta=input('Deseja continuar?[S/N]').upper()
    if resposta=='N':
        break

for c in range(0,contador):
    tam=len(tupla[2*c])
    pon=20-tam

    print(tupla[2*c],'.'*pon,'R$', tupla[2*c+1])


