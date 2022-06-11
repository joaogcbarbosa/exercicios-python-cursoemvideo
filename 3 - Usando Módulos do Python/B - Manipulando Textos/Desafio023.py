#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: 1984
#Unidade: 4
#Dezena: 8
#Centena: 9
#Milhar: 1
num = str(input('Digite um número: '))
num_novo = num.replace(num, '000' + num)
print(f'Unidade: {num_novo[-1]}')
print(f'Dezena: {num_novo[-2]}')
print(f'Centena: {num_novo[-3]}')
print(f'Milhar: {num_novo[-4]}')
