lista_nomes=[]
lista_notas1=[]
lista_notas2=[]
lista_medias=[]


resposta='S'
while resposta=='S':
    nome=input('Digite o nome: ')
    lista_nomes.append(nome)
    nota1=float(input('Digite a primeira nota: '))
    lista_notas1.append(nota1)
    nota2=float(input('Digite a segunda nota: '))
    lista_notas2.append(nota2)
    media=(nota1+nota2)/2
    lista_medias.append(media)
    resposta=str(input('Quer continuar? [S/N] ')).upper()
print('No',' '*4,'Nome',' '*6,'Media')
print('-'*30)
for c in range(0,len(lista_nomes)):
    tam=len(lista_nomes[c])
    esp=15-tam
    print(c,' '*2,lista_nomes[c],' '*esp,lista_medias[c])
desc=int(input('Mostrar as notas de qual aluno em especifico? (999 para parar): '))
if desc==999:
    print('Fim do programa!')




while desc!=999:
    if desc<len(lista_nomes):
        print('As notas de {} foram {} e {}'.format(lista_nomes[desc],lista_notas1[desc],lista_notas2[desc]))
        desc = int(input('Mostrar as notas de qual aluno em especifico? (999 para parar): '))
    elif desc>=len(lista_nomes):
        desc = int(input('Tente novamente.Mostrar as notas de qual aluno em especifico? (999 para parar): '))


