#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from time import sleep
num = float(input('Insira um número: '))
print('PROCESSANDO...')
sleep(1)
print(f'Dobro: {num*2:.0f}')
print(f'Triplo: {num*3:.0f}')
print(f'Raiz quadrada: {num**(1/2):.2f}')
