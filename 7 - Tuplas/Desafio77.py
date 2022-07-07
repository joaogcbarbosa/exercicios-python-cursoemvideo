#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Casa', 'Mato', 'Celular', 'Borracha', 'Dinheiro', 'Som', 'Papel', 'Quadro', 'Caderno')

for palavra in palavras:
    print(f'\nAs vogais de {palavra.upper()} são:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
