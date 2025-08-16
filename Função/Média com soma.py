def soma(a, b):
    return a + b

total = 0

for i in range(4):

    num = float(input(f"Digite a sua {i + 1} nota: "))
    total = soma(total, num)

media = total / 4

print(f"Media: {media:.2f}")

if media >= 6:
    print("Aprovado")

else:
    print("Reprovado")