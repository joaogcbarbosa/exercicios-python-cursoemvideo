# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(txt):
    for letra in txt:
        print('=', end='')
    print(f'\n{txt}')
    for letra in txt:
        print('=', end='')


msg = str(input('Digite algo: ')).strip()
escreva(msg)

# Solução do professor:

def escreva(txt):
    tam = len(txt) + 4
    print('='*tam)
    print(txt.center(tam))
    print('='*tam)


msg = str(input('Digite algo: ')).strip()
escreva(msg)
