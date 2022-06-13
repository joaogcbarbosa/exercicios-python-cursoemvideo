#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
inverso = ''
frase = str(input('Digite uma frase: ')).strip().upper()
fraseSeparada = frase.split()
fraseJunta = ''.join(fraseSeparada)
for c in range(len(fraseJunta) - 1, -1, -1):
   inverso += fraseJunta[c]
if fraseJunta == inverso:
    print('É um palíndromo.')
else:
    print('Não é um pálíndromo.')
