#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
from time import sleep
distancia = int(input('Qual será a distância da sua viagem(Km)? '))
print('Calculando o preço da sua passagem...')
sleep(1)
if distancia <= 200:
    print(f'Sua passagem custará R${distancia*0.50:.2f}!')
else:
    print(f'Sua passagem custará R${distancia*0.45:.2f}!')
