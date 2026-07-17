def leiaINT(msg):

    loop=True
    while loop==True:
        entrada = (input(msg))
        try:
            numero=int(entrada)

            loop=False
        except:
            if entrada.strip()=='':
                print( 'Digitou um valor vazio')
            else:
                print( f'Erro, pois "{entrada.upper()}" nao eh um numero inteiro.')
            loop=True
    return numero

def leiaREAL(msg):
    loop = True
    while loop == True:
        entrada = (input(msg))
        try:
            numero = float(entrada)

            loop = False
        except:
            if entrada.strip() == '':
                print('Digitou um valor vazio')
            else:
                print(f'Erro, pois "{entrada.upper()}" nao eh um numero real.')
            loop = True
    return numero

inteiro=leiaINT('Digite o numero inteiro: ')
real=leiaREAL('Digite o numero real: ')
print(f'O inteiro eh {inteiro} e o real eh {real}')
