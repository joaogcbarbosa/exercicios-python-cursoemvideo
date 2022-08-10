#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade do preço é R${moeda.metade(preco)} ')
print(f'O dobro do preço é R${moeda.dobro(preco)}')
print(f'O preço com 10% de aumento é {moeda.aumentar(preco, 10):.2f}')
