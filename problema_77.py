lista=[]
vogais=('a','e','i','o','u')

palavra=str(input('Digite uma palavra, se quiser parar, digite "PARAR": ').lower().strip())
lista.append(palavra)
while palavra!='parar':
    palavra=str(input("Digite outra palavra: ")).lower().strip()
    lista.append(palavra)
lista.remove('parar')
tup=tuple(lista)

for c in range(0,len(tup)):
    teste=[]
    tam=len(tup[c])
    for d in range(0,tam):
        if tup[c][d] in vogais:
            teste.append(tup[c][d])
    imp=str(teste)
    imp2=' '.join(teste).upper()
    print('A palavra {} possui as vogais: {} '.format(tup[c].upper(),imp2))








