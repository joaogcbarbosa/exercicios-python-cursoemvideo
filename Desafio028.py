#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário vence ou perde.
from random import randint
from time import sleep
print('='*20)
print('JOGO DA ADIVINHAÇÃO')
print('='*20)
num_pc = randint(0, 5)
print('Computador: Pensei em um número entre 0 e 5. Tente adivinhar!')
sleep(3)
num_jogador = int(input('Jogador: Acho que você escolheu o número: '))
if num_pc == num_jogador:
    print('-Você acertou!')
else:
    print(f'Computador: Você errou! Eu escolhi o número {num_pc}.')
