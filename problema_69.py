lista1=['SIM','S','NAO','N']
lista2=['MASCULINO','MASC','M','F','FEM','FEMININO']
cont1=0
cont2=0
cont3=0
lista3=['F','FEM','FEMININO']
lista4=['M','MASC','MASCULINO']
lista5=['SIM','S']

sexo=str(input('Digite o sexo: ')).upper()
while sexo not in lista2:
    sexo=str(input('Digite certo. Qual o sexo? ')).upper()
if sexo in lista4:
        cont2 = cont2 + 1
idade=int(input("Qual a idade da pessoa? "))
while idade<0:
    idade=int(input("Digite certo. Qual a idade da pessoa?"))
if idade > 18:
        cont1 = cont1 + 1
if sexo in lista3 and idade<=20:
        cont3=cont3+1

resposta=str(input('Voce quer continuar? ')).upper()
while resposta not in lista1:
    resposta=str(input('Digite certo. Voce quer continuar? ')).upper()
while resposta in lista5:
    sexo = str(input('Digite o sexo: ')).upper()
    while sexo not in lista2:
        sexo = str(input('Digite certo. Qual o sexo? ')).upper()
    if sexo in lista4:
            cont2 = cont2 + 1
    idade = int(input("Qual a idade da pessoa?"))
    while idade < 0:
        idade = int(input("Digite certo. Qual a idade da pessoa?"))
    if idade > 18:
            cont1 = cont1 + 1
    if sexo in lista3 and idade<=20:
        cont3=cont3+1
    resposta = str(input('Voce quer continuar? ')).upper()

print('Ok, terminamos por aqui! Ha {} pessoa(s) com mais de 18 anos, {} homem/homens e {} mulheres com menos de 20 anos.'.format(cont1,cont2,cont3))




