#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar ao usuário se ele quer ou não continuar.No final mostre: A)Quantas pessoas têm mais de 18 anos; B)Quantos homens foram cadastrados; C)Quantas mulheres têm menos de 20 anos.
cont_idade = cont_masc = cont_idade_fem = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':
        while sexo not in 'MF':
            sexo = str(input('Entrada inválida. Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo in 'M':
        cont_masc += 1
    if sexo in 'F':
        if idade < 20:
            cont_idade_fem += 1
    escolha = str(input('Deseja continuar cadastrando dados [S/N]? ')).strip().upper()[0]
    if escolha not in 'SN':
        while escolha not in 'SN':
            escolha = str(input('Entrada inválida. Deseja continuar cadastrando dados [S/N]? ')).strip().upper()[0]
    if escolha in 'S':
        continue
    if escolha in 'N':
        break
print(f'{cont_idade} pessoas têm mais de 18 anos;')
print(f'{cont_masc} homens foram cadastrados.')
print(f'{cont_idade_fem} mulheres têm menos de 20 anos.')
