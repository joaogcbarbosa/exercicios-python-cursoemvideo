#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os "n" primeiros elementos de uma sequência de fibonacci.
n = int(input('Digite a quantidade de termos que deseja ver na sequência de Fibonacci: '))
t0 = 0
t1 = 1
print(f'{t0} -> {t1}', end=' -> ')
cont = 3
while cont <= n:
    t2 = t0 + t1
    print(f'{t2}', end=' -> ')
    cont += 1
    t0 = t1
    t1 = t2
print('Fim')
