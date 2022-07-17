#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lsita_par = []
lista_imp = []
c = 0

while True:
    lista.append(int(input('Digite um número: ')))
    if lista[c] % 2 == 0:
        lsita_par.append(lista[c])
    else:
        lista_imp.append(lista[c])
    c += 1
    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Entrada inválida. Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break

print(f'Lista completa: {lista}')
print(f'Lista de números pares: {lsita_par}')
print(f'Lista de números ímpares: {lista_imp}')
