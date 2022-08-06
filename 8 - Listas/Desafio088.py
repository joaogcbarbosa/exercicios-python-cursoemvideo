#Faça um programa que ajude um jogador a criar palpites. O programa vai perguntar quantos jogos serão gerados e sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

jogos = list()
aux = list()

n = int(input('Quantos jogos você quer? '))

for i in range(n):
    while True:
        rand_num = randint(1, 60)
        if rand_num in aux:
            continue
        else:
            aux.append(rand_num)
            aux.sort()
        if len(aux) == 6:
            break
    jogos.append(aux[:])
    aux.clear()

for i in range(n):
    print(f'Jogo {i + 1}: {jogos[i]}')
