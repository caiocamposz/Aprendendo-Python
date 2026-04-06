linha_0=[]
linha_1=[]
linha_2=[]

for c in range (0,3):
    num0=int(input("Digite o numero para a posicao (0,{}) : ".format(c)))
    linha_0.append(num0)
for c in range (0,3):
    num1=int(input("Digite o numero para a posicao (1,{}) : ".format(c)))
    linha_1.append(num1)
for c in range (0,3):
    num2=int(input('Digite o numero para a posicao (2,{}) : '.format(c)))
    linha_2.append(num2)

c=0
print('[ {} ] [ {} ] [ {} ]'.format(linha_0[c],linha_0[c+1],linha_0[c+2]))
print('[ {} ] [ {} ] [ {} ]'.format(linha_1[c],linha_1[c+1],linha_1[c+2]))
print('[ {} ] [ {} ] [ {} ]'.format(linha_2[c],linha_2[c+1],linha_2[c+2]))


CODIGO MELHOR:
linha_0=[]
linha_1=[]
linha_2=[]
matriz=[linha_0,linha_1,linha_2]
for c in range (0,3):
    for d in range (0,3):
        num=int(input('Digite o valor para a posicao ({},{}): '.format(d,c)))
        matriz[c].append(num)
print('[{}] [{}] [{}]'.format(linha_0[0],linha_0[1],linha_0[2]))
print('[{}] [{}] [{}]'.format(linha_1[0],linha_1[1],linha_1[2]))
print('[{}] [{}] [{}]'.format(linha_2[0],linha_2[1],linha_2[2]))
