#Faça um programa que leia a temperatura em °C e converta para °F e °K.
from time import sleep
print('='*24)
print('CONVERSOR DE TEMPERATURA')
print('='*24)
sleep(0.5)
temperatura = float(input('Temperatura em °C: '))
print('Convertendo...')
temperaturaK = temperatura+273
temperaturaF = temperatura*1.8+32
sleep(1)
print(f'Em °K: {temperaturaK:.1f}')
print(f'Em °F: {temperaturaF:.1f}')
