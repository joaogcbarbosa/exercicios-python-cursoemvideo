#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
cont = s = 0
while True:
    num = int(input('Digite um número: '))
    cont += 1
    s += num
    if num == 999:
        break
print(f'A soma entre todos {cont - 1} números inseridos foi {s - 999}')
