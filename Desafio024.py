#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade_split = cidade.upper().split()
print('O nome da cidade começa com "Santo"?')
print('SANTO' in cidade_split[0])
