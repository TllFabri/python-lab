def soma(a, b):
    return a + b

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
num_3 = float(input("Digite o terceiro número: "))

soma1 = soma(num_1, num_2)
total = soma(soma1, num_3)

print(f"{num_1} + {num_2} + {num_3} = {total}")