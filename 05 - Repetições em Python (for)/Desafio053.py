#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
inverso = ''
frase = str(input('Digite uma frase: ')).strip().upper()
frase_sep = frase.split()
frase_junta = ''.join(frase_sep)
for c in range(len(frase_junta) - 1, -1, -1):
   inverso += frase_junta[c]
if frase_junta == inverso:
    print('É um palíndromo.')
else:
    print('Não é um pálíndromo.')
