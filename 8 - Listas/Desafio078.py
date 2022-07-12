#Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

valores = []
maior = menor = 0

for c in range(1, 6):
    valores.append(int(input(f'{c}º número: ')))

for c in range(0, 5):
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'O maior valor inserido foi {maior}')
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{maior} na posição {pos}')

print(f'O menor valor inserido foi {menor}')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{menor} na posição {pos}')
