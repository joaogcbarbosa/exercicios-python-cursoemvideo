#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar ao usuário se vai continuar. No final mostre: A)Qual é o total gasto na compra; B)Quantos produtos custam mais de R$1000; C)Qual é o nome do produto mais barato.
total = cont_prod = preco_mais_barato = 0
prod_mais_barato = ''
while True:
    prod = str(input('Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000.00:
        cont_prod += 1
    if cont_prod == 1:
        preco_mais_barato = preco
        prod_mais_barato = prod
    else:
        if preco < preco_mais_barato:
            preco_mais_barato = preco
            prod_mais_barato = prod
    escolha = str(input('Deseja adicionar mais produtos [S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Entrada inválida. Deseja adicionar mais produtos [S/N]? ')).strip().upper()[0]
    if escolha in 'S':
        continue
    else:
        break
print(f'O total gasto na compra foi R${total:.2f};')
print(f'{cont_prod} produtos custam mais de R$1000.00;')
print(f'O produto mais barato é {prod_mais_barato}.')
