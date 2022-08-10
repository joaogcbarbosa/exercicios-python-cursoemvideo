#Crie um programa que leia o nome da pessoa e diga se tem ou não "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip()
nome_upper = nome.upper()
print('Seu nome tem "Silva"?')
print('SILVA' in nome_upper)
