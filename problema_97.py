frase=str(input("Digite umas palavras: "))
corr=frase.strip()
def func(a):
    tam=len(a)
    print('='*(tam+6))
    print('   {}   '.format(a))
    print('=' * (tam + 6))

func(corr)
