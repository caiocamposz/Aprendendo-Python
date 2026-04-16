import random
dados={}
resultados=[]
for c in range(0,4):
    escolha = random.randint(1,6)
    dados[c]=escolha
    print('O jogador {} tirou {}. '.format(c,escolha))
print('-'*30)
print('Resultado Final')
res=dados.items()


func=lambda item: item[1] # meio que define uma funcao ( def ) e da pra usar assim
res_final=sorted(res,key=func,reverse=True)

for c in range(0,4):
    print('{}o Lugar: Jogador {}, pois tirou {}. '.format(c+1,res_final[c][0],res_final[c][1]))


