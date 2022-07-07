#Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Deposi disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = menor = 0
num1 = randint(1, 10)
num2 = randint(1, 10)
num3 = randint(1, 10)
num4 = randint(1, 10)
num5 = randint(1, 10)
numeros = (num1, num2, num3, num4, num5)
print('Os números gerados foram:')
for c in numeros:
    print(c, end=' ')
print('\nO maior número gerado foi {};'.format(max(numeros)))
print('O menor número gerado foi {}.'.format(min(numeros)))

#OUTRA RESOLUÇÃO:

#from random import randint
#maior = menor = 0
randNums = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'A tupla formada foi {randNums}')
for c in range(0, 5):
    if c == 0:
        maior = menor = randNums[c]
    else:
        if randNums[c] > maior:
            maior = randNums[c]
        if randNums[c] < menor:
            menor = randNums[c]
print(f'O maior valor encontrado na tupla é {maior}')
print(f'O menor valor encontrado na tupla é {menor}')