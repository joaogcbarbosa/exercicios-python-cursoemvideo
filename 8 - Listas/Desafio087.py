#Aprimore o desafio anterior, mostrando no final: a) a soma de todos valores pares digitados; b) a soma dos valores da terceira coluna; c)o maior valor da segunda linha.

mat = []
aux = []
soma_par = 0
mai_seg_lin = 0

for i in range(3):
    for j in range(3):
        aux.append(int(input(f'Valor {i + 1}x{j + 1}: ')))
        if aux[j] % 2 == 0:
            soma_par += aux[j]
    mat.append(aux[:])
    aux.clear()

print('     MATRIZ')
for c in range(len(mat)):
    print(f'{mat[c][0]:^5}{mat[c][1]:^5}{mat[c][2]:^5}')
    if c == 0:
        mai_seg_lin = mat[1][c]
    elif mat[1][c] > mai_seg_lin:
        mai_seg_lin = mat[1][c]

soma_terc_col = mat[0][2] + mat[1][2] + mat[2][2]

print()
print(f'A soma de todos valores pares da matriz é {soma_par}')
print(f'A soma de todos valores da terceira coluna é {soma_terc_col}')
print(f'O maior valor da segunda linha é {mai_seg_lin}')
