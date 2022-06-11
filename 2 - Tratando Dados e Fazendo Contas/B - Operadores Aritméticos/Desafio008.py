#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
from time import sleep
print('='*21)
print('CONVERSOR DE MEDIDAS')
print('='*21)
medida = float(input('Insira uma medida em metros: '))
print('Convertendo...')
sleep(1)
print(f'Em centímetros: {medida*100:.2f}.')
print(f'Em milímetros: {medida*1000:.2f}.')
