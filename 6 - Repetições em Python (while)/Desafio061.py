#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressao mas usando WHILE
n = -1
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
while n < 9:
    n += 1
    an = a1 + n*r
    print(an, end=' -> ')
print('Fim')
