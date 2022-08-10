#Faça um programa que leia a altura e largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
from time import sleep
from math import ceil
altura = float(input('Altura da sua parede(m): '))
largura = float(input('Largura da sua parede(m): '))
sleep(0.5)
print('A área da sua parede é {:.2f}m²...Vou calcular quanto de tinta você precisa.'.format(altura*largura))
sleep(3)
area_parede = altura*largura
tinta = area_parede/2
print(f'Você precisa de {ceil(tinta)} litros de tinta!') #usar "ceil" pois não pode faltar tinta