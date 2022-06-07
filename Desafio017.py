#Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
#mostre o comprimento da hipotenusa.
from math import hypot
from time import sleep
print('Cálculo de Hipotenusa')
sleep(1)
catOp = float(input('Cateto Oposto: '))
catAd = float(input('Cateto Adjacente: '))
hip = hypot(catAd, catOp)
print(f'A hipotenusa vale {hip:.2f}.')
