#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.
from time import sleep
num = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1)
print(f'Seu antecessor é {num - 1} e seu sucessor é {num + 1}')
