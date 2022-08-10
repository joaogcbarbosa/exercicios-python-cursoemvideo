#Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.

import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade do preço é {moeda.moeda(moeda.moeda(preco))}')
print(f'O dobro do preço é {moeda.moeda(moeda.dobro(preco))}')
print(f'O preço com 10% de aumento é {moeda.moeda(moeda.aumentar(preco, 10))}')
