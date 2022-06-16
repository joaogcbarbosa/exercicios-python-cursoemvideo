#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mais 0 termos.
n = -1
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
while n < 9:
    n += 1
    an = a1 + n*r
    print(an)
    termos = int(input('Quantos termos quer a mais? '))
    if termos > 0:
        n = 9 + termos
    if termos == 0:
        break
print('Programa encerrado.')
