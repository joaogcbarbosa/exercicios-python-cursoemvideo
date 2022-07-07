#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 a 20. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
       escolha = int(input('Digite um número entre 0 e 20: '))
       if 0 <= escolha <= 20:
              break
       print('Fora dos limites. Tente novamente. ', end='')
for c in range(0, len(num)):
       if c == escolha:
              print(f'Você digitou o número {num[c]}.')

#Outra forma:
#Substituir o laço for por print('Você digitou o número {}.'.format(num[escolha]))