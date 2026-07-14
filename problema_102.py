def fatorial(num,a):
    ex=num
    for c in range(1,num):
        num=num*c
    if a==True:
        if num == 0:
            return '0! = 1'
        else:
            for c in range(1,ex):
                print(ex+1-c,end=' x ')
            return f'1 = {num}'
    else:
        if num == 0:
            return '0! = 1'
        else:
            return num

numero=int(input('Digite um numero: '))
quer=str(input('Quer ver o passo a passo? [S/N] ').upper())

if quer == 'S':
    resp = True
else:
    resp = False

print(fatorial(numero,resp))
