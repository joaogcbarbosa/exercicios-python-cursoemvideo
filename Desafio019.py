#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nome do escolhido.
from random import choice
from time import sleep
a1 = str(input('Primeiro aluno: ')).strip().upper()
a2 = str(input('Segundo aluno: ')).strip().upper()
a3 = str(input('Terceiro aluno: ')).strip().upper()
a4 = str(input('Quarto aluno: ')).strip().upper()
lista = [a1, a2, a3, a4]
escolha = choice(lista)
print('Sorteando...')
sleep(1)
print('O(a) aluno(a) escolhido(a) para apagar o quadro foi {}.'.format(escolha))
