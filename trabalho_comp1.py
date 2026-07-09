nome=str(input("Qual o nome da sua empresa? "))
print('====Analisando o estoque====')
resposta='SIM'
quantidade_total=0
valor_total=0
contador2=1
produtos=[]
while resposta=='SIM' or resposta=='S':
    print("="*30)
    print(f'Cadastrando o {contador2}o produto...')
    contador2 = contador2 + 1
    produto=str(input("Qual o produto? ").capitalize())
    categoria=str(input("Qual a categoria? ").capitalize())
    quantidade=int(input("Qual a quantidade? "))
    custo=float(input("Qual o custo unitário? "))

    cadastro = {"produto": produto,"categoria": categoria,"quantidade": quantidade,"custo": custo}
    produtos.append(cadastro)
    quantidade_total=quantidade_total+quantidade
    valor_total=valor_total+(custo*quantidade)
    resposta=str(input("Deseja continuar? [Sim/Nao ou S/N] ").upper())
print("=" * 30)
print(f'Relatório Final da empresa {nome.upper()}')
print("-" * 30)
print('No   Produto              Valor Total')
cont=0
for c in produtos:
    valor = c["quantidade"] * c["custo"]
    espacos_produto = 20 - len(c["produto"])

    print(cont, "  ", c["produto"], " "*espacos_produto, valor)
    cont = cont + 1
print('-'*30)
print(f'Quantidade total do estoque: {quantidade_total}')
print(f'Valor total do estoque: {valor_total}')
print("=" * 30)
info=0
while info!=999:
    info = (int(input('Deseja ter mais informações sobre algum produto? Digite o numero dele [ 999 Para Sair ]: ')))
    if info == 999:
        break
    while info != 999 and (info >= cont or info < 0):
        print('Ops, esse produto nao existe!')
        info = int(input('Tente novamente [999 Para Sair]: '))

    if info != 999:
        produto_escolhido = produtos[info]

        print("=" * 30)
        print("Produto:", produto_escolhido["produto"])
        print("Categoria:", produto_escolhido["categoria"])
        print("Quantidade:", produto_escolhido["quantidade"])
        print("Custo unitário:", produto_escolhido["custo"])
        print("Valor total:", produto_escolhido["quantidade"] * produto_escolhido["custo"])
        print("=" * 30)

print('Finalizando...')
