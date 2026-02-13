numero=int(input("digite um numero: "))
while numero<0 or numero>10:
    numero=int(input("Tente novamente. digite um numero: "))
lista=['zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez']
print(lista[numero])
