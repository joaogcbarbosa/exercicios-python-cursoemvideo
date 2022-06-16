#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre eles e qual foi o menor e maior valor inserido. O programa deve perguntar ao usuário se ele quer continuar a digitar valores.
num = cont = soma = maior = menor = 0
escolha = ''
while escolha in 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    media = soma/cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break
print(f'A média entre os {cont} valores inseridos é igual a {soma/cont}.')
print(f'O maior número é {maior} e o menor é {menor}')
