def maior(lista):
    print('Analisando os valores...')
    print(*lista ,f'Foram digitados {len(lista)} valores.')
    print(f'O maior valor informado foi {max(lista)}')

lista=[]
resposta='S'
while resposta=='S':
    num=int(input('Digite um valor: '))
    lista.append(num)
    resposta=input('Deseja continuar? [S/N] ').upper()
maior(lista)

