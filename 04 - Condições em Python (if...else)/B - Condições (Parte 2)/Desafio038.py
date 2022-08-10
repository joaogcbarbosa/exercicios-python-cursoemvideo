#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a seguinte mensagem:
#O primeiro valor é maior
#O segundo valor é maior;
#Não existe valor maior, os dois são iguais.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
if n1 > n2:
    print('O primeiro número é maior que o segundo.')
elif n2 > n1:
    print('O segundo número é maior que o primeiro.')
elif n1 == n2:
    print('Ambos números são iguais.')
