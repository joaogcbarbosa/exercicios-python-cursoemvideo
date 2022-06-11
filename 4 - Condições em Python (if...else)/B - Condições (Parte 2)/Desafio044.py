#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: à vista dinheiro/cheque: 10% de desconto; à vista no cartão: 5% de desconto; em até 2x no cartão:preço normal; 3x ou mais no cartão: 20% de juros.
valor = float(input('Insira o preço do produto: R$'))
print("""[1] À vista no dinheiro ou cheque: 10% de desconto;
[2] À vista no cartão: 5% de desconto;
[3] Até 2x no cartão: preço normal;
[4] 3x ou mais no cartão: 20% de juros.""")
escolha = int(input('Qual das opções de pagamento deseja efetuar (1, 2, 3 ou 4)? '))
if escolha == 1:
    print(f'Com 10% de desconto o valor do produto cai de R${valor:.2f} para R${valor*0.90:.2f}')
elif escolha == 2:
    print(f'Com 5% de desconto o valor do produto cai de R${valor:.2f} para R${valor*0.95:.2f}')
elif escolha == 3:
    print(f'O valor do produto é R${valor:.2f} e será dividido em duas parcelas de R${valor/2:.2f}')
elif escolha == 4:
    print(f'Com 20% de juros o valor do produto vai de R${valor:.2f} para R${valor*1.20:.2f}. O produto será dividido '
          f'em 3 parcelas de R${valor*1.20/3:.2f}.')
