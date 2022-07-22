#Crie um programa que tenha a função leiaInt(), que vai funcionar semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um número: ')

def leia_int(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            return f'Você digitou o número {num}.'
        else:
            print('Você não digitou um inteiro. Tente novamente.')
            continue


num = leia_int('Digite um número inteiro: ')
print(num)
