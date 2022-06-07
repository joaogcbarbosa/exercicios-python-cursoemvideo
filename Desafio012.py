#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
from time import sleep
preco = float(input('Insira o preço do produto: R$'))
print('Calculando desconto...')
sleep(1)
print(f'O preço do produto com 5% de desconto é R${preco*0.95:.2f}')
