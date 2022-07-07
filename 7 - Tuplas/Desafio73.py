#Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: a)apenas os cinco primeiros colocados; b)os últimos quatro colocados da tabela; c)uma lista com os times em ordem alfabética; d)em que posição na tabela está o time da chapecoense.

time = ('Corinthians', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avaí', 'América-MG',
         'Chapecoense', 'Palmeiras', 'Internacional', 'Fluminense', 'Goiás', 'Cuiabá', 'Athletico-PR',
         'Flamengo', 'Juventude', 'Ceará SC', 'Atlético-GO', 'Fortaleza')

print('CINCO PRIMEIROS COLOCADOS:')
print(time[0])
print(time[1])
print(time[2])
print(time[3])
print(time[4])
print('ÚLTIMOS QUATRO COLOCADOS:')
print(time[16])
print(time[17])
print(time[18])
print(time[19])
print('TODOS TIMES EM ORDEM ALFABÉTICA:')
print(sorted(time))
print('POSIÇÃO DA CHAPECÓ:')
print(time.index('Chapecoense') + 1)

#OUTRA RESOLUÇÃO:

print(f'Cinco primeiros colocados: {time[0:6]}')
print(f'Últimos quatro colocados: {time[-4:]}')
print(f'Em ordem alfabetica: {sorted(time)}')
print(f'Chapecoense está na posição {time.index("Chapecoense") + 1}')