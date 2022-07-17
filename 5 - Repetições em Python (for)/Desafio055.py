#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor dos pesos lidos.
maior_peso = menor_peso = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso registrado foi {maior_peso}kg e o menor foi {menor_peso}kg')
