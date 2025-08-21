def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

temperaturas = [-5, 0, 20, 37, 100]

print("\nConversão de Temperaturas °C → °F")
print("-" * 35)
print(f"{'Celsius (°C)':<15}{'Fahrenheit (°F)':>15}")
print("-" * 35)

for c in temperaturas:
    f = celsius_para_fahrenheit(c)
    print(f"{c:<15}{f:>15.1f}")
