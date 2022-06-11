#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar;
#Se é a hora de se alistar;
#Se já passou do tempo de alistamento.
#O programa também deve mostrar quanto falta para o prazo ou quanto passou.
from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNasc
anoAlistamento = anoNasc + 18
if idade == 18:
    print('Você está com 18 anos, deve se alistar.')
elif idade > 18:
    print('Você deveria ter se alistado há {} anos.'.format(anoAtual-anoAlistamento))
elif idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format(anoAlistamento-anoAtual))
