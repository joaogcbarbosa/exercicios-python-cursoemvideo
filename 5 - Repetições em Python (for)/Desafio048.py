#Faça um programa que calcule a soma entre todos números ímpares que são múltiplos de 3 e que se encontram no intervalo entre 1 e 500.
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(f'A soma é igual a {soma}')
      