#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
from time import sleep
salario = float(input('Digite seu salário: R$'))
print('Calculando seu aumento...')
sleep(1)
print(f'Parabéns!Seu novo salário é de R${salario*1.15:.2f}')
