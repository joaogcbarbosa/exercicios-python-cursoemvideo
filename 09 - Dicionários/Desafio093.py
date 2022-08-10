#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em casa partida. No final, tudo isso será guardado num dicionário, incluindo o total de gols feitos durante o campeonato.

dados = dict()
gols = list()

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(partidas):
    gols.append(int(input(f'  Quantos gols na {c + 1}ª partida? ')))
    dados['gols'] = gols
    dados['total'] = sum(gols)

print('='*56)
print(dados)
print('='*56)

for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('='*56)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas. ')
for c in range(len(gols)):
    print(f'  => Na partida {c}, fez {gols[c]} gols')
print(f'Foi um total de {dados["total"]} gols.')
