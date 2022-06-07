#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nome
#dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
from time import sleep
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
print('Sorteando...')
sleep(1.5)
print('A ordem de apresentação dos trabalhos será:')
shuffle(lista)
print(lista)
