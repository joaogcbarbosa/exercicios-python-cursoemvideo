#Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
theta = float(input('Insira um ângulo qualquer em graus: '))
theta_rad = radians(theta)
print(f'Seno: {sin(theta_rad):.2f}')
print(f'Cosseno: {cos(theta_rad):.2f}')
print(f'Tangente: {tan(theta_rad):.2f}')
#Esse exercício tem alguns erros, como por exemplo: a tangente de 90º é indefinida matematicamente, mas o programa re-
#torna um valor. Visto que o objetivo do exercício é treinar a importação de bibliotecas, os erros não são cruciais.
