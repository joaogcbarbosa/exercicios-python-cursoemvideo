#fatorial
fat = 1
c = 2
num = int(input('Digite um número para ver o fatorial: '))
num += 1
while num >= c:
    num -= 1
    fat *= num
print(f'O fatorial é {fat}')
