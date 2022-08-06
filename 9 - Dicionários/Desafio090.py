#Faça um programa que leia nome e média de um aluno, guardando também a situação num dicionário. No final, mostre o conteúdo da estrutura na tela

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] < 5.0:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] < 7.0:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print()

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
