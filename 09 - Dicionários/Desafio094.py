#Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a) quantas pessoas foram cadastradas; b) a média de idade do grupo; c) uma lista com todas as mulheres; d) uma lista com todas pessoas com idade acima da média.

pessoas = list()
s_idade = 0
mulheres = list()

while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]

    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas "M" ou "F"')
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]

    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa.copy())
    pessoa.clear()

    escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

    while escolha not in 'SN':
        print('ERRO! Por favor, digite apenas "M" ou "F"')
        escolha = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if escolha in 'N':
        break

for c in range(len(pessoas)):
    s_idade += pessoas[c]['idade']
    if pessoas[c]['sexo'] in 'F':
        mulheres.append(pessoas[c]['nome'])

m_idade = s_idade/len(pessoas)

print('='*50)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {m_idade:.0f} anos')
print(f'C) As mulheres cadastradas foram {mulheres}: ')
print(f'D) Lista das pessoas com idade acima da média:')
for c in range(len(pessoas)):
    if pessoas[c]['idade'] > m_idade:
        print(f'nome = {pessoas[c]["nome"]}; sexo = {pessoas[c]["sexo"]}; idade = {pessoas[c]["idade"]} ')
