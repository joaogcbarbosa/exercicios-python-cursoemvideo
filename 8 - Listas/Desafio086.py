#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

mat = []
aux = []

for i in range(1, 4):
    for j in range(1, 4):
        aux.append(int(input(f'Valor {i}x{j}: ')))
    mat.append(aux[:])
    aux.clear()

for c in range(len(mat)):
    print(f'{mat[c][0]:^5}{mat[c][1]:^5}{mat[c][2]:^5}')
