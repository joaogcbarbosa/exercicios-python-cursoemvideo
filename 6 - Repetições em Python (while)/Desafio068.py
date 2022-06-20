#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER. Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep
cont_vit_par = cont_vit_impar = 0
print('='*12)
print('PAR OU ÍMPAR')
print('='*12)
sleep(1)
while True:
    print("""    [1] Par;
    [2] Ímpar.""")
    escolha = int(input('Qual você escolhe [1/2]? '))
    computador = randint(0, 5)
    jogador = int(input('Jogador: '))
    if escolha == 1:
        if (jogador + computador) % 2 == 0:
            cont_vit_par += 1
            print(f'Ganhou! Você escolheu {jogador} e eu escolhi {computador}.')
        else:
            break
    if escolha == 2:
        if (jogador + computador) % 2 != 0:
            cont_vit_impar += 1
            print(f'Ganhou! Você escolheu {jogador} e eu escolhi {computador}.')
        else:
            break
if (cont_vit_impar + cont_vit_par) == 0:
    print('Venci! Você não ganhou nenhuma vez.')
else:
    print(f'Perdeu! Eu escolhi {computador}. Mas você ganhou {cont_vit_par + cont_vit_impar} vezes!')
