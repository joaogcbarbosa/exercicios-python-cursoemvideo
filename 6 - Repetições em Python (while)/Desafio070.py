#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar ao usuário se vai continuar. No final mostre: A)Qual é o total gasto na compra; B)Quantos produtos custam mais de R$1000; C)Qual é o nome do produto mais barato.
total = contProduto = precoMaisBarato = 0
produtoMaisBarato = ''
while True:
    produto = str(input('Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000.00:
        contProduto += 1
    if contProduto == 1:
        precoMaisBarato = preco
        produtoMaisBarato = produto
    else:
        if preco < precoMaisBarato:
            precoMaisBarato = preco
            produtoMaisBarato = produto
    escolha = str(input('Deseja adicionar mais produtos [S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Entrada inválida. Deseja adicionar mais produtos [S/N]? ')).strip().upper()[0]
    if escolha in 'S':
        continue
    else:
        break
print(f'O total gasto na compra foi R${total:.2f};')
print(f'{contProduto} produtos custam mais de R$1000.00;')
print(f'O produto mais barato é {produtoMaisBarato}.')
