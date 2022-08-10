#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os dez primeiros termos dessa progressão.
print('PROGRESSÃO ARITMÉTICA')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a10 = a1 + 10*r
print('Os dez primeiros termos dessa P.A são:')
for c in range(a1, a10, r):
    print(f'{c}', end=' -> ')
print('Fim')
