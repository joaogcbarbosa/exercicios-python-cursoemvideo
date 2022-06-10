#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a Média atingida:
#Média abaixo de 5.0: REPROVADO;
#Média entre 5.0 e 6.9: RECUPERAÇÃO;
#Média 7.0 ou maior: APROVADO.
print('='*16)
print('CÁLCULO DE MÉDIA')
print('='*16)
n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
media = (n1+n2)/2
if media < 5.0:
    print(f'Sua média foi {media:.2f}. REPROVADO')
elif 5.0 < media < 7.0:
    print(f'Sua média foi {media:.2f}. RECUPERAÇÃO')
elif media >= 7.00:
    print(f'Sua média foi {media:.2f}. APROVADO')
