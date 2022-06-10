#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais, calcule um aumento de 15%.
from time import sleep
salario = float(input('Insira o valor do seu salário: R$'))
print('Calculando seu aumento...')
sleep(1)
if salario > 1250:
    print(f'O seu salário com aumento de 10% é de R${salario*1.10:.2f}.')
if salario <= 1250:
    print(f'O seu salário com aumento de 15% é de R${salario*1.15:.2f}.')
