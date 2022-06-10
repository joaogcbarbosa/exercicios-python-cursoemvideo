#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro nome: Ana
#Último nome: Souza
from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
nome_split = nome.split()
primeiro_nome = nome_split[0]
ultimo_nome = nome_split[(len(nome_split) - 1)]
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')
