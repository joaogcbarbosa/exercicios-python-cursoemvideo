#Desenvolva um programa que leia o comprimento de três retas, diga ao usuário se elas podem ou não formar um triângulo e se esse triângulo é equilátero, isósceles ou escaleno.
from time import sleep
print('='*23)
print('ANALISADOR DE TRIÂNGULO')
print('='*23)
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Compriento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('É possível formar um triângulo com essas medidas e ele seria equilátero!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r1 != r3 or r2 == r3 != r1 or r3 == r2 != r1 or r3 == r1 != r2:
        print('É possível formar um triângulo com essas medidas e ele seria isósceles!')
    elif r1 != r2 != r3:
        print('É possível formar um triângulo com essas medidas e ele seria escaleno!')
else:
    print('Não é possível formar um triângulo com essas medidas.')
