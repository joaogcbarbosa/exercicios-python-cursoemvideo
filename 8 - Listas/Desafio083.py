#Crie um programa onde uma usuário digita uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""rightP = leftP = 0
exp = str(input('Digite uma expressão matemática: '))
expList = exp.split()
for conta in expList:
    for element in conta:
        leftP += element.count('(')
        rightP += element.count(')')
if leftP == rightP:
    print('Expressão matemática válida!')
else:
    print('Expressão com erro nos parênteses.')""" #Com essa resolução, expressões como "(a*b)-)c(=12" estariam corretas.

#Resolução certa:

exp = str(input('Digite a expressão: '))
pilha = []
for element in exp:
    if element == '(':
        pilha.append('(')
    elif element == ')':
        if len(pilha) > 0:
            pilha.pop() #O par de parênteses é formado, então pode-se eliminar o único parêntese "(" na pilha .
        else:
            pilha.append(')') #Parêntese adicionado se antes não foi encontrado o seu par.
            break
if len(pilha) == 0:
    print('Expressão matemática válida!')
else:
    print('Expressão com erro nos parênteses.')
