#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aux = list()
alunos = list()

while True:
    aux.append(str(input('Nome: ')).strip().upper())
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    m = (aux[1] + aux[2]) / 2
    aux.append(m)
    alunos.append(aux[:])
    aux.clear()

    dec = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if dec in 'N':
        break

print('='*25)
print('    Nº     Nome    Média')
for c in range(len(alunos)):
    print(f'{c:^9}{alunos[c][0]:^9}{alunos[c][3]:^9}')
print('='*25)

while True:
    escolha = int(input('Deseja ver as notas de qual aluno? (999 interrompe) Nº'))
    if escolha == 999:
        break
    print(f'As notas de {alunos[escolha][0]} são {alunos[escolha][1]} e {alunos[escolha][2]}')
print('PROGRAMA ENCERRADO')
