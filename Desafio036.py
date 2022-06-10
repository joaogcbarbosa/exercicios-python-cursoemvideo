#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Insira o valor do imóvel: R$'))
salario = float(input('Insira seu salário: R$'))
anos = int(input('Em quantos anos deseja financiar? '))
meses = anos*12
prestacao = valor/meses
if prestacao > salario*0.30:
    print(f'Empréstimo negado! A prestação de R${prestacao:.2f} excede 30% do valor do seu salário.')
else:
    print(f'Empréstimo aprovado! O valor da prestação será de R${prestacao:.2f}')
