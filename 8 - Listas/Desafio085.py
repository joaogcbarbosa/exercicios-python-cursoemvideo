#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastrá-los em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

nums = [[], []]

for c in range(7):
    num = int(input(f'{c + 1}º número: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

nums[0].sort()
nums[1].sort()

print(f'Os números pares são {nums[0]}')
print(f'Os números ímpares são {nums[1]}')
