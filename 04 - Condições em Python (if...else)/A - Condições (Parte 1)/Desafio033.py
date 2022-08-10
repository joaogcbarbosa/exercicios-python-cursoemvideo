#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from time import sleep
print('Digite três números!')
sleep(1.5)
n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
n3 = int(input('Terceiro: '))
if n1 > n2 > n3:
    print(f'{n1} é o maior e {n3} é o menor.')
if n2 > n1 > n3:
    print(f'{n2} é o maior e {n3} é o menor.')
if n3 > n1 > n2:
    print(f'{n3} é o maior e {n2} é o menor.')
if n1 > n3 > n2:
    print(f'{n1} é o maior e {n2} é o menor.')
if n2 > n3 > n1:
    print(f'{n2} é o maior e {n1} é o menor.')
if n3 > n2 > n2:
    print(f'{n3} é o maior e {n2} é o menor.')
