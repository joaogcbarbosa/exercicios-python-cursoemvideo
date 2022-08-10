#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar;
#Se é a hora de se alistar;
#Se já passou do tempo de alistamento.
#O programa também deve mostrar quanto falta para o prazo ou quanto passou.
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nasc
ano_alist = ano_nasc + 18
if idade == 18:
    print('Você está com 18 anos, deve se alistar.')
elif idade > 18:
    print('Você deveria ter se alistado há {} anos.'.format(ano_atual-ano_alist))
elif idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format(ano_alist-ano_atual))
