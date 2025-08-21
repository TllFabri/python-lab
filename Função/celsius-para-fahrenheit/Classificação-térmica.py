def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def classificar(f):
    if f <= 50:
        return "Frio"
    elif 51 <= f <= 77:
        return "Ameno"
    else:
        return "Quente"

temperaturas = [-5, 0, 20, 37, 100]

print("\nConversão de Temperaturas °C → °F")
print("-" * 55)
print(f"{'Celsius (°C)':<15}{'Fahrenheit (°F)':>15}{'Classificação':>20}")
print("-" * 55)

for c in temperaturas:
    f = celsius_para_fahrenheit(c)
    tipo = classificar(f)
    print(f"{c:<15}{f:>15.1f}{tipo:>20}")
