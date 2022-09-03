#Crie um programa onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista, já na posição correta
#de inserção (sem usar o sort()).No final, mostre a lista ordenada na tela.

#nums = []

#for i in range(1, 6):
#    nums.append(int(input(f'{i}º Número: ')))
#for i in range(0, 4):
#    for j in range(i + 1, 5):
#        if nums[i] > nums[j]:
#            aux = nums[i]
#            nums[i] = nums[j]
#            nums[j] = aux
#for i in range(0, 5):
#    print(nums[i], end=' ')

#OUTRA RESOLUÇÃO:

nums = [int(input(f'{i + 1}º Número: ')) for i in range(5)]

for i in range(4):
    for j in range(i + 1, 5):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)
