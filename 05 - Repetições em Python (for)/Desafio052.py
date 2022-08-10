#Faça um programa que leia um número inteiro e diga se ele é primo ou não.
cont = 0
num = int(input('Digite um número para saber se ele é primo: '))
for c in range(1, num + 1):
    if num % c == 0 and num % num == 0:
        cont += 1
if cont == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo.')
