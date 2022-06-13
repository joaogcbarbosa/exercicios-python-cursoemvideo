#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos no ano novo, indo de 10 até 0 com intervalos de 1s.
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!')
