#crie um programa que leia dois valores e crie um menu na tela: 1 somar, 2 multiplicar, 3 maior, 4 novos numeros 5 sair do programa. seu programa deverá executar a ação em cada caso
escolha = ''
while escolha in 'S':
    num1 = float(input('Primeiro valor: '))
    num2 = float(input('Segundo valor: '))
    print('='*25)
    print("""Opções:
    [1] Somar;
    [2] Multiplicar;
    [3] Maior;
    [4] Novos valores;
    [5] Sair do programa;""")
    print('='*25)
    opcao = int(input('Qual ação deseja executar? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre os valores inseridos é {soma}')
    if opcao == 2:
        produto = num1 * num2
        print(f'O produto entre os valores inseridos é {produto}')
    if opcao == 3:
        if num1 > num2:
            maior = num1
            print(f'O maior valor inserido é {maior}')
        else:
            maior = num2
            print(f'O maior valor inserido é {maior}')
    if opcao == 4:
        continue
    if opcao == 5:
        break
    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
print('Programa encerrado.')
