# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(nums):
    maior_num = max(nums)
    print(f'O maior valor inserido foi {maior_num}')


valores = []
while True:
    valores.append(int(input('Digite um número inteiro: ')))

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Entrada inválida. Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break

maior(valores)


# Sem o uso das funções max() e min():


def maior(nums):  
    maior_num = 0
    for c in range(0, len(nums)):
        if c == 0:
            maior_num = menor_num = nums[c]
        else:
            if nums[c] > maior_num:
                maior_num = nums[c]

    print(f'O maior valor inserido foi {maior_num}')


valores = []
while True:
    valores.append(int(input('Digite um número inteiro: ')))

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Entrada inválida. Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break

maior(valores)


# Abordagem sugerida pelo professor:


def maior(*nums):
    maior_num = 0
    for c in range(0, len(nums)):
        if c == 0:
            maior_num = nums[c]
        else:
            if nums[c] > maior_num:
                maior_num = nums[c]

    print(f'Dentro dos números {nums}, o maior valor encontrado foi {maior_num}')
    print('=~'*35)


maior(1, 5, -2, 3, 10)
maior(2, 6, 3, 11)
maior(52, 23, 44, 19)
maior(11, 28)
maior()
