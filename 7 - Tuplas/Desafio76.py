#Crie um programa que tenha uma tupla única com o nome de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular.

compras = ('Shampoo', 'R$9.99', 'Sabonete', 'R$0.99', 'Soro fisiológico', 'R$5.99', 'Manteiga de cacau', 'R$1.99', 'Bandaid', 'R$3.99')

for c in range(0, len(compras)):
    if c % 2 == 0:
        print(f'{compras[c]:.<25}', end='')
    else:
        print(f'{compras[c]}')
        