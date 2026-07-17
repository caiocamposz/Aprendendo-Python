def notas(*notas,situacao=False):
    sit=''
    dicionario = {}
    maior=max(notas)
    menor=min(notas)
    media=sum(notas)/len(notas)
    dicionario['Total']=len(notas)
    dicionario['Maior Nota']=maior
    dicionario['Menor Nota']=menor
    dicionario['Media']=media
    if situacao==True:
        if 8<=media<=10:
            sit='BOM'
        elif 6<=media<8:
            sit='RAZOAVEL'
        else:
            sit='RUIM'
        dicionario['Situacao']=sit
    return dicionario

lista=[]
cont=1
resposta='S'
numero=0
while resposta=='S':
    numero = float(input(f'Digite a nota do {cont}o aluno: '))
    lista.append(numero)
    cont=cont+1
    resposta=input('Quer continuar? [S/N]').upper()
quer=str(input('Quer mostrar a situacao da turma? [S/N]').upper())
if quer=='S':
    quer=True
else:
    quer=False

print(notas(*lista,situacao=quer))
