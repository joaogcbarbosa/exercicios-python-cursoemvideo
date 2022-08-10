#Crie um programa que leia um número inteiro qualquer e que diga se ele é par ou ímpar.

print('='*20)
print('JOGO DE PAR OU ÍMPAR')
print('='*20)
num = int(input('Digite um número inteiro qualquer: '))
if num % 2 == 0:
    print('Par!')
else:
    print('Ímpar!')
