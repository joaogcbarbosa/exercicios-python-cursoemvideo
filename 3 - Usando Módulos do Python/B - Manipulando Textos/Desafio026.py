#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece pela primeira vez;
#Em que posição ela aparece pela última vez.
from time import sleep
frase = str(input('Digite um frase: ')).strip()
frase_junta = frase.replace(' ', '')
print('Analisando a letra "A"')
sleep(1)
print(f'Aparece {frase.upper().count("A")} vezes;')
print(f'Aparece pela primeira vez na posição {frase_junta.upper().find("A") + 1};')
print(f'Aparece pela última vez na posição {frase_junta.upper().rfind("A") +1 }.')
