#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoa = dict()
ano_atual = datetime.today().year

pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = ano_atual - nasc
ctps = int(input('Carteira de trabalho (0 se não tem): '))

if ctps == 0:
    pessoa['ctps'] = ctps

    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')

else:
    pessoa['ctps'] = ctps
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['contratação'] + 35 - ano_atual)

    for k, v in pessoa.items():
        print(f'-{k} tem o valor {v}')
