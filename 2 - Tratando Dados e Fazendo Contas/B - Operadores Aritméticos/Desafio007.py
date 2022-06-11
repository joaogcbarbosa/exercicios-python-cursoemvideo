#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
from time import sleep
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
print('Calculando média...')
media = (nota1+nota2)/2
sleep(1)
print(f'Sua média é {media:.2f}')
