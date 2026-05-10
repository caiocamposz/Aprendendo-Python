lista=[]
contagem=0
media=0
resposta='S'
while resposta=='S':
    dic={}
    dic['nome']=input('Digite o nome: ').capitalize()
    dic['sexo']=input('Digite o sexo (M/F): ').upper()
    dic['idade']=int(input('Digite a idade: '))
    contagem=contagem+1
    media=media+dic['idade']
    lista.append(dic)

    resposta=str(input('Quer continuar? [S/N]: ')).upper()
media=media/contagem
lista2=[]
for c in range(0,len(lista)):
    if lista[c]['sexo']=='F':
        lista2.append(lista[c]['nome'])
lista3=[]
for c in range(0,len(lista)):
    if lista[c]['idade']>media:
        lista3.append(lista[c]['nome'])
lista2=', '.join(lista2)
lista3=', '.join(lista3)

print('=-'*30)
print('a) O total de pessoas eh {}'.format(contagem))
print('b) A media de idade eh {:.1f}'.format(media))
if len(lista2)==0:
    print('c) Nao ha mulheres no grupo')
else:
    print('c) O nome de todas as mulheres: {}'.format(lista2))
print('d) O nome das pessoas com idade maior que {:.1f} anos: {}'.format(media,lista3))
