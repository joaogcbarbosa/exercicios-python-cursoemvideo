#Melhore o jogo 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint
chutes = 1
print('='*19)
print('JOGO DA ADIVINHAÇÃO')
print('='*19)
sleep(1.75)
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10. Tenta adivinhar!')
jogador = int(input('Seu chute: '))
while jogador != computador:
    jogador = int(input('Errou! Tente novamente: '))
    chutes += 1
if chutes == 1:
    print('Você acertou de primeira!')
else:
    print(f'Acertou! Você precisou de {chutes} chutes para adivinhar.')
