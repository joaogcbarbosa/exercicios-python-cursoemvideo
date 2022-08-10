#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = -1
soma = -999
while True:
    num = int(input(f'{cont+2}º número: '))
    cont += 1
    soma += num
    if num == 999:
        break
print(f'Soma = {soma}')
print(f'Média = {soma/cont:.2f}')
