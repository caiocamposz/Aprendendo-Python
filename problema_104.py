def leiaINT(frase):
    a=input(frase)
    if a=='':
        b=a
    elif a[0]=='-':
        b=a.replace(a[0],'',1)
    else:
        b=a
    while b.isnumeric() is False:
        print('ERRO!')
        a=input(frase)
        if a == '':
            b = a
        elif a[0] == '-':
            b = a.replace(a[0], '', 1)
        else:
            b = a
    return f'Seu numero eh {a}.'

print(leiaINT('Digite um numero inteiro: '))
