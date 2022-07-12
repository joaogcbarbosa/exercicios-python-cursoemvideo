#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a)Quantos números foram digitados; b)A lista de valores, ordenada de forma decrescente; c)Se o valor 5 foi digitado e está ou não na lista.

nums = []
cont = tem5 = 0

while True:
    nums.append(int(input('Digite um valor: ')))
    if nums[cont] == 5:
        tem5 += 1
    cont += 1
    nums.sort(reverse=True)
    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Entrada inválida. Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break

print(f'Foram digitados {cont} números')
print(f'A lista na ordem decrescente é {nums}')

if tem5 != 0:
    print(f'O número 5 foi encontrado {tem5} vezes na lista.')
else:
    print('O número 5 não foi encontrado na lista.')
