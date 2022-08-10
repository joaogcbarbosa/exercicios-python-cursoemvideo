#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status. Abaixo de 18.5 = abaixo do peso; entre 18.5 e 25.0 = peso ideal; 25.0 até 30.0 = sobrepeso; 30.0 até 40.0 = obesidade
#acima de 40.0 = obesidade mórbida
print('='*14)
print('CÁLCULO DO IMC')
print('='*14)
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/altura**2
if imc < 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25.0:
    print('Seu IMC é {:.1f}. Você está no peso ideal.'.format(imc))
elif 25.0 <= imc < 30.0:
    print('Seu IMC é {:.1f}. Você está com sobrepeso.'.format(imc))
elif 30.0 <= imc < 40.0:
    print('Seu IMC é {:.1f}. Você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está com obesidade mórbida.'.format(imc))
