#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


escolha = ''
while True:
    n = input('Digite um número inteiro para ver seu fatorial: ')

    if n.isnumeric():
        n = int(n)

        escolha = str(input('Deseja ver o cálculo do fatorial [S/N]? ')).strip().upper()
        if escolha in '':
            print('Você não digitou nada. Repetindo...')
            continue
        while escolha not in 'SN':
            escolha = str(input('Entrada inválida. Deseja ver o cálculo do fatorial [S/N]? ')).strip().upper()
        if escolha in 'S':
            escolha = True
            break
        else:
            escolha = False
            break
    else:
        print('Você não digitou um número inteiro. Repetindo...')
        continue

resp = fatorial(n, escolha)

if escolha:
    print(f'{resp}')
else:
    print(f'O fatorial de {n} é {resp}')
