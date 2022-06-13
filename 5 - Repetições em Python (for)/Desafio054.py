#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.
from datetime import date
contMaior = contMenor = 0
anoAtual = date.today().year
for c in range(1, 8):
    nascimento = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = anoAtual - nascimento
    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1
print(f'{contMaior} pessoas são maiores de idade e {contMenor} são menores.')
