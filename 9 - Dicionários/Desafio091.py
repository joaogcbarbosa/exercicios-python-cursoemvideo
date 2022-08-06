#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.

from random import randint
from operator import itemgetter

rnkg = list()
rst = dict()

rst['jogador1'] = randint(1, 6)
rst['jogador2'] = randint(1, 6)
rst['jogador3'] = randint(1, 6)
rst['jogador4'] = randint(1, 6)

for k, v in rst.items():
    print(f'{k} tirou {v} no dado.')
print()

rnkg = sorted(rst.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(rnkg):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    