resposta='S'
contador=0
nome_pesado=[]
peso_pesado=0
nome_leve=[]
peso_leve=0
while resposta=='S':
    nome=str(input('Digite o nome: '))
    peso=int(input('Digite o peso: '))
    contador=contador+1
    if contador==1:
        peso_pesado=peso
        nome_pesado=[nome]
        peso_leve=peso
        nome_leve=[nome]
    else:
        if peso>peso_pesado:
            peso_pesado=peso
            nome_pesado=[nome]
        elif peso==peso_pesado:
            nome_pesado.append(nome)
        if peso<peso_leve:
            peso_leve=peso
            nome_leve=[nome]
        elif peso==peso_leve:
            nome_leve.append(nome)
    resposta=str(input('Voce deseja continuar?(S/N) ').upper())
print('Ha {} pessoas'.format(contador))
print('O maior peso eh {} e quem possui eh {}'.format(peso_pesado,nome_pesado))
print('O menor peso eh {} e quem possui eh {}'.format(peso_leve,nome_leve))
