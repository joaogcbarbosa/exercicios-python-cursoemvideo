#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até um valor correto.
"""while True:
    sexo = str(input('Insira seu sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'MF':
        break
print(f'Sexo {sexo} registrado. Obrigado!')"""

sexo = str(input('Insira seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Entrada inválida. Insira seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado. Obrigado!')
