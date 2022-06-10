#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas letras maiúsculas;
#O nome com todas letras minúsculas;
#Quantas letras no total sem considerar espaços;
#Quantas letras têm o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Com letras maiúsculas: {nome.upper()};')
print(f'Com letras minúsculas: {nome.lower()};')
nome_junto = nome.replace(' ', '')
print(f'O nome tem um total de {len(nome_junto)} letras;')
nome_split = nome.split()
print(f'O primeiro nome tem {len(nome_split[0])} letras.')
