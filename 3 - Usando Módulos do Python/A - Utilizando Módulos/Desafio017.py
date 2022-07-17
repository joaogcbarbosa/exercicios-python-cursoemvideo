#Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
#mostre o comprimento da hipotenusa.
from math import hypot
from time import sleep
print('Cálculo de Hipotenusa')
sleep(1)
cat_op = float(input('Cateto Oposto: '))
cat_ad = float(input('Cateto Adjacente: '))
hip = hypot(cat_ad, cat_op)
print(f'A hipotenusa vale {hip:.2f}.')
