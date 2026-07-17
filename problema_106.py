def ajuda_python():
        ajuda = ''
        while ajuda != 'fim':
            ajuda = str(input('Em qual funcao/biblioteca voce precisa de ajuda? ').lower())

            if ajuda == 'fim':
                print('Ok, finalizando...')
                break


            frase=len(f'Acessando o manual do comando "{ajuda}"')
            print(frase*'=')
            print(f'Acessando o manual do comando "{ajuda}"')
            print(frase * '=')
            help(ajuda)
            print(frase * '=')

ajuda_python()
