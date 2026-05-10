nome=str(input("Qual o seu nome? "))
ano=int(input("Qual o ano de nascimento? "))
carteira=int(input("Qual o numero da sua carteira de trabalho (0 SE NAO TEM) ? "))
if carteira==0:
    dic1={'nome':nome,'idade':2026-ano,'carteira':carteira}
    for chave,valor in dic1.items():
        print('{} tem o valor de {}'.format(chave,valor))
else:
    contratacao=int(input('Digite o ano de contratacao: '))
    salario=int(input('Digite o salario em reais: '))
    dic2={'nome':nome,'idade':2026-ano,'carteira':carteira,'contratacao':contratacao,'salario':salario,'aposentadoria':contratacao+35-ano}
    for chave,valor in dic2.items():
        print('{} tem o valor de {}'.format(chave,valor))
