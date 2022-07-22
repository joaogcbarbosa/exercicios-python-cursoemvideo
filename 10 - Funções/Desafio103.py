# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(j='', g=0):
    if j in '':
        j = 'NÃO INFORMADO'
    return f'O jogador {j} marcou {g} gol(s).'


jogador = str(input('Nome do jogador: ')).strip()

if jogador.isnumeric():
    print('Você não digitou um nome. Tente novamente.')
    while jogador.isnumeric():
        jogador = str(input('Nome do jogador: ')).strip()
        if not jogador.isnumeric():
            break

gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

resp = ficha(jogador, gols)
print(resp)
