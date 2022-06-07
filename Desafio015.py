#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dia pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.
from time import sleep
distancia = float(input('Quantos Km você percorreu com o carro? '))
dias = int(input('Por quantos dias? '))
print('Calculando o total a pagar pelo aluguel...')
preco = 0.15*distancia + 60*dias
sleep(1.5)
print(f'O total a pagar é R${preco:.2f}')
