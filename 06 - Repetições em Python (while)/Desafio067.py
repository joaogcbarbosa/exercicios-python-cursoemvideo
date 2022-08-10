#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número inserido for negativo.
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num > 0:
        for c in range(1, 11):
            print(f'{num} X {c} = {num*c}')
    else:
        break
print('Programa encerrado.')
