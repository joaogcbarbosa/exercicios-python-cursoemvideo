#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por km/h acima do limite. Calcule essa multa.

v = int(input('Insira sua velocidade atual(Km/h): '))
if v > 80:
    valor_multa = 7*(v-80)
    print('MULTADO!')
    print(f'Você ultrapassou a velocidade limite (80Km/h) e terá que pagar uma multa de R${valor_multa:.2f}.')
    print('Tenha um bom dia e dirija com segurança!')
else:
    print('Tenha um bom dia e dirija com segurança!')
