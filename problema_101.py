def voto(a):
    idade=2026-a
    if idade<16:
        return(f'Com {idade} anos, voce NAO VOTA. ')
    elif 16 <= idade < 18 or idade>65:
        return(f'Com {idade} anos, o seu voto eh OPCIONAL')
    else:
        return(f'Com {idade} anos, voce VOTA OBRIGATORIAMENTE')

ano=int(input('Digite o seu ano de nascimento: '))
while ano<=0 or ano>2026:
    ano=int(input('Tente novamente! Digite corretamente o seu ano de nascimento: '))
print(voto(ano))
