#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = list()
dados = dict()
gols = list()

while True:
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(partidas):
        gols.append(int(input(f'  Quantos gols na {c + 1}ª partida? ')))
        dados['gols'] = gols[:]
        dados['total'] = sum(gols)

    jogadores.append(dados.copy())
    dados.clear()
    gols.clear()

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break

print('='*40)
print(f'cod            Nome           Gols          Tot')
for c in range(len(jogadores)):
    print(f'{c!s:<15s}{jogadores[c]["nome"]!s:<15s}{jogadores[c]["gols"]!s:<15s}{jogadores[c]["total"]!s:<15s}')

while True:
    dec = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dec == 999:
        break
    elif dec < 0 or dec > (len(jogadores) - 1):
        print(f'Não existe jogador com código {dec}!')
    else:
        print('='*30)
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[dec]["nome"].upper()}:')
        for gol in jogadores[dec]['gols']:
            c = 1
            print(f'No {c}º jogo fez {gol} gols.')
            c += 1
        print('=' * 30)

print('PROGRAMA ENCERRADO')
