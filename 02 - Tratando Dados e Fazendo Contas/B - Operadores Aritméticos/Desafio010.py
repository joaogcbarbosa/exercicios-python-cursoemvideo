#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00=R$5,06.
from time import sleep
print('CONVERSOR DE MOEDAS')
sleep(0.5)
valor_reais = float(input('Quantos reais você tem na carteira? R$'))
valor_dolares = valor_reais/5.06
print('Convertendo para dólares...')
sleep(1.5)
print(f'Você pode comprar US${valor_dolares:.2f}!')
