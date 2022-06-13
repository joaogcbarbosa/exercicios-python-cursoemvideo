#Refaça o Desafio009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando laço for.
num = int(input('Digite um número para mostrar sua tabuada: '))
for c in range(0, 11):
    print(f'{num}  X {c: >2} = {num*c: >2}')
