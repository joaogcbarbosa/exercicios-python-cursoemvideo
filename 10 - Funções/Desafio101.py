#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import date


def voto(nasc):
    if idade >= 18:
        return 'Voto OBRIGATÓRIO'
    elif 16 <= idade < 18:
        return 'Voto OPCIONAL'
    else:
        return 'Voto NEGADO'


ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
resp = voto(ano_nasc)
print(f'Você tem ou irá completar {idade} anos de idade. {resp}')
