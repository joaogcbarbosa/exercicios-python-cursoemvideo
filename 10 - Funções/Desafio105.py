#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: -quantidade de notas; -a maior nota; -a menor nota; -a média da turma; -a situação. Adicione também as docstrings da função.

def notas(*n, sit=False):
    inf = dict()

    inf['Total de notas'] = len(n)
    inf['Maior nota'] = max(n)
    inf['Menor nota'] = min(n)
    inf['Média'] = sum(n)/len(n)
  # Dicionário recebendo valores de uma Tupla

    if sit:
        if inf['Média'] >= 7.0:
            inf['Situação'] = 'Bom'
        elif inf['Média'] >= 5.0:
            inf['Situação'] = 'Razoável'
        else:
            inf['Situação'] = 'Ruim'
    return inf


resp = notas(6.5, 9.0, 7.5, sit=True)
print(resp)
