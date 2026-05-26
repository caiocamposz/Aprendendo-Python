def contador(i,f,p):
    if p<0:
        p=-p
    if p==0:
        p=1
    print('='*40)
    print(f'Contagem de {i} ate {f}, de {p} em {p}')
    sequencia=[]
    if f>i:
        for c in range(i,f+1):
            sequencia.append(c)
    else:
        for c in range(f,i+1):
            sequencia.append(c)
        sequencia.sort(reverse=True)
    a=sequencia[::p]
    print(*a,'FIM!')


contador(1,10,1)
contador(10,0,2)

print('Agora eh sua vez de personalizar a contagem!')
inicio=int(input('Inicio da contagem: '))
fim=int(input('Fim: '))
p=int(input('Passo: '))
contador(inicio,fim,p)
