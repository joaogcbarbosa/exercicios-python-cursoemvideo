#Crie um programa que faça o computador jogar jokenpô com você.
from random import randint
from time import sleep
print('~'*7)
print('JOKENPÔ')
print('~'*7)
sleep(1)
print("""[1] Pedra;
[2] Papel;
[3] Tesoura.""")
jogador = int(input('Faça sua escolha (1, 2 ou 3): '))
print('JO')
sleep(0.75)
print('KEN')
sleep(0.75)
print('PÔ!')
computador = randint(1, 3)
if jogador == computador:
    if jogador == 1:
        print('Empate! Nós dois escolhemos Pedra.')
    elif jogador == 2:
        print('Empate! Nós dois escolhemos Papel.')
    else:
        print('Empate! Nós dois escolhemos Tesoura.')
elif jogador == 1 and computador == 2:
    print('Você escolheu Pedra e eu escolhi Papel. Eu ganhei!')
elif jogador == 1 and computador == 3:
    print('Você escolheu Pedra e eu escolhi Tesoura. Você ganhou!')
elif jogador == 2 and computador == 1:
    print('Você escolheu Papel e eu escolhi Pedra. Você ganhou!')
elif jogador == 2 and computador == 3:
    print('Você escolheu Papel e eu escolhi Tesoura. Eu ganhei!')
elif jogador == 3 and computador == 1:
    print('Você escolheu Tesoura e eu escolhi Pedra. Eu ganhei!')
elif jogador == 3 and computador == 2:
    print('Você escolheu Tesoura e eu escolhi Papel. Você ganhou!')
