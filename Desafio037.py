#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:binário, octal ou hexadecimal.
from time import sleep
print('='*17)
print('CONVERSOR DE BASE')
print('='*17)
sleep(1.75)
num = int(input('Digite o número que deseja converter: '))
print("""[1] Converter para binário;
[2] Converter para octal;
[3] Converter para hexadecimal.""")
escolha = int(input('Qual conversão gostaria de fazer (1, 2 ou 3)? '))
if escolha == 1:
    print('O número {} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
