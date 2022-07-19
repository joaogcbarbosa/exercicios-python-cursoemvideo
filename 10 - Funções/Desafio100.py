# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia():
    for c in range(0, 5):
        nums.append(randint(1, 100))
    print(f'Os números sorteados foram {nums}')


def soma_par():
    s = 0
    for c in range(0, 5):
        if nums[c] % 2 == 0:
            s += nums[c]
    print(f'A soma entre todos valores pares sorteados é igual a {s}.')


nums = []
sorteia()
soma_par()
