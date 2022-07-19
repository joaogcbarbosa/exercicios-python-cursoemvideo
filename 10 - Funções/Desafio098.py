# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de um em um; b) de 10 até 0, de 2 em 2; c) uma contagem personalizada.

from time import sleep


def contador(ini, fim, pas):
    if pas == 0:
        pas = 1
    if pas < 0:
        pas = 1

    if ini < fim:
        print(f'Contando de {ini} até {fim} no passo {pas}:')
        for c in range(ini, fim + 1, pas):
            sleep(0.5)
            print(c, end=' -> ')
        print('Fim!')

    else:
        print(f'Contando de {ini} até {fim} no passo {pas}:')
        for c in range(ini, fim - 1, -pas):
            sleep(0.5)
            print(c, end=' -> ')
        print('Fim!')


contador(1, 10, 1)
print()

contador(10, 0, 2)
print()

print('CONTAGEM PERSONALIZADA')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

contador(i, f, p)
