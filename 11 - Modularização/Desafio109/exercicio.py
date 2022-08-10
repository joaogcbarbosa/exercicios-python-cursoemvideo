#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade do preço é {moeda.metade(preco, True)}')
print(f'O dobro do preço é {moeda.dobro(preco, True)}')
print(f'O preço com 10% de aumento é {moeda.aumentar(preco, 10, True)}')
