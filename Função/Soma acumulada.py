def soma(a, b):
    return a + b

num = int(input('Digite os números que deseja somar: '))

total = 0

for i in range(num):
    numero = float(input(f'Digite {i + 1} número: '))
    total = soma(total, numero)

print(f'A soma dos {num} númeors é {total}')
