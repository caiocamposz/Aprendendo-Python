soma=0
soma_terc=0
linha_0=[]
linha_1=[]
linha_2=[]
matriz=[linha_0,linha_1,linha_2]
for c in range (0,3):
    for d in range (0,3):
        num=int(input('Digite o valor para a posicao ({},{}): '.format(c,d)))
        matriz[c].append(num)
        if num%2==0:
            soma=soma+num
        if d==2:
            soma_terc=soma_terc+num
print('[{}] [{}] [{}]'.format(linha_0[0],linha_0[1],linha_0[2]))
print('[{}] [{}] [{}]'.format(linha_1[0],linha_1[1],linha_1[2]))
print('[{}] [{}] [{}]'.format(linha_2[0],linha_2[1],linha_2[2]))
print('a) A soma dos numeros pares eh ',soma)
print('b) A soma da terceira coluna eh ',soma_terc)
maior_seg=max(matriz[1])
print('c) O maior valor da 2a linha eh ',maior_seg)
