def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

try:
    inicio = int(input("Digite a temperatura inicial em °C: "))
    fim = int(input("Digite a temperatura final em °C: "))

    if inicio > fim:
        print("O valor inicial deve ser menor ou igual ao final.")
    else:
        print("\nTabela de Conversão °C → °F (de 2 em 2 graus)")
        print("-" * 35)
        print(f"{'Celsius (°C)':<15}{'Fahrenheit (°F)':>15}")
        print("-" * 35)
        for c in range(inicio, fim + 1, 2):
            f = celsius_para_fahrenheit(c)
            print(f"{c:<15}{f:>15.1f}")
except ValueError:
    print("Entrada inválida! Digite apenas números inteiros.")
