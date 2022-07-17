#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Mirim (até 9 anos); Infantil (até 14 anos); Junior (até 19 anos); Sênior (até 20 anos); Master (Acima)
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento do atleta: '))
idade = ano_atual - ano_nasc
if idade < 9:
    print('Categoria MIRIM')
elif idade < 14:
    print('Categoria INFANTIL')
elif idade < 19:
    print('Categoria JUNIOR')
elif idade < 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
