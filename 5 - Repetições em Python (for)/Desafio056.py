#Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa mostre: A média de idade do grupo; Qual é o nome do homem mais velho; Quantas mulheres têm menos de 20 anos.
s = contFem = maisVelho = 0
nomeMaisVelho = ''
for c in range(1, 5):
    nome = str(input(f'Nome da {c}ª pessoa: ')).strip().upper()
    idade = int(input('Idade: '))
    s += idade
    while True:
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo in 'M':
            if c == 1:
                maisVelho = idade
                nomeMaisVelho = nome
            else:
                if idade > maisVelho:
                    maisVelho = idade
                    nomeMaisVelho = nome
        if sexo in 'F':
            if idade < 20:
                contFem += 1
        if sexo in 'MF':
            break
print(f'A média de idade do grupo é {s/4:.0f}')
print(f'O nome do homem mais velho é {nomeMaisVelho}')
print(f'{contFem} mulheres têm menos de 20 anos.')
#Esse exercício deveria ser feito apenas com o laço "for", porém quando refiz achei mais intuitivo mesclar com "while".
