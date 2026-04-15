dados={}
dados['nome']=str(input('Digite o nome: '))
dados['media']=int(input('Digite o media: '))
if dados['media']>7:
    sit='aprovado'
else:
    sit='reprovado'
print('Nome eh igual a {}, media eh igual a {} e a situacao final eh {}'.format(dados['nome'],dados['media'],sit.upper()))
