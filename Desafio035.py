#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep
print('='*24)
print('Analisador de Triângulos')
print('='*24)
sleep(2)
print('Insira o comprimento de três retas')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
print('Analisando...')
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo com essas medidas!')
else:
    print('Não é possível formar um triângulo com essas medidas.')
