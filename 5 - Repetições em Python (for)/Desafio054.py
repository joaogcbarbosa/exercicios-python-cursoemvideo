#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.
from datetime import date
cont_maior = contMenor = 0
ano_atual = date.today().year
for c in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        cont_maior += 1
    else:
        contMenor += 1
print(f'{cont_maior} pessoas são maiores de idade e {contMenor} são menores.')
