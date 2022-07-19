# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(c, l):
    a = c * l
    print(f'A área do terreno {c}x{l} é de {a:.2f}m²')


comp = float(input('Comprimento (m): '))
larg = float(input('Largura (m): '))
area(comp, larg)
