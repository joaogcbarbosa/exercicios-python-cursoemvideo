#Faça um programa que leia o nome e peso de várias pesoas, guardando tudo em uma lista. No final, mostre: a) quantas pessoas foram cadastradas; b) uma listagem com as pessoas mais pesadas; c) Uma listagem com as pessoas mais leves.

dados = list()
pessoas = list()
mais_leve = mais_pesado = 0
nomes_mais_pesados = list()
nomes_mais_leves = list()
c = 0

while True:
    print(f'{c + 1}ª PESSOA')
    dados.append(str(input('Nome: ')))  # dados[0]
    dados.append(float(input('Peso: ')))  # dados[1]

    if c == 0:
        mais_pesado = mais_leve = dados[1]
    else:
        if dados[1] > mais_pesado:
            mais_pesado = dados[1]
        if dados[1] < mais_leve:
            mais_leve = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    c += 1

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')

for pessoa in pessoas:
    if pessoa[1] == mais_pesado:
        nomes_mais_pesados.append(pessoa[0])
    if pessoa[1] == mais_leve:
        nomes_mais_leves.append(pessoa[0])

print(f'Os mais pesados são {nomes_mais_pesados}')
print(f'Os mais leves são {nomes_mais_leves}')
