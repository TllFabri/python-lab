def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

# Programa principal
try:
    c = float(input("Digite a temperatura em °C: "))
    f = celsius_para_fahrenheit(c)
    print(f"{c:.1f}°C equivalem a {f:.1f}°F")
except ValueError:
    print("Entrada inválida! Digite um número.")
