#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor dos pesos lidos.
maiorPeso = menorPeso = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maiorPeso = menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print(f'O maior peso registrado foi {maiorPeso}kg e o menor foi {menorPeso}kg')
