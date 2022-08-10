#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre: a)quantas vezes apareceu o valor 9; b)em que posição foi digitado o primeiro valor 3; c)quais foram os numeros pares.

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))
valor4 = int(input('Quarto valor: '))
valores = (valor1, valor2, valor3, valor4)
print('O valor "9" apareceu {} vezes.'.format(valores.count(9)))
if 3 in valores:
    print('O primeiro valor "3" apareceu na posição {}'.format(valores.index(3) + 1))
else:
    print('O número três não apareceu nenhuma vez.')
print('Valores que são pares:')
for valor in valores:
    if valor % 2 == 0:
        print(f'{valor}')
