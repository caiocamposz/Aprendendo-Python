lista_par=[]
lista_impar=[]

for c in range(1,8):
    num = int(input('Digite o {}o numero: '.format(c)))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print('A sua lista de numeros pares eh: {}'.format(sorted(lista_par)))
print('A lista de numeros impares eh: {}'.format(sorted(lista_impar)))

