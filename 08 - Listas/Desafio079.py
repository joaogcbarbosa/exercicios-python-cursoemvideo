#Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

nums = []
while True:
    num = int(input('Digite um número: '))
    if num not in nums:
        nums.append(num)
    else:
        print('Número já inserido anteriormente. Não computado.')
    nums.sort()
    escolha = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Entrada inválida. Deseja continuar[S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break
print(f'Lista de números: {nums}')
