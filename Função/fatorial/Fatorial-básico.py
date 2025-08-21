def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def calcular_fatorial():
    try:
        n = int(input("Digite um inteiro não negativo: "))
        if n < 0:
            print("Por favor, insira um número não negativo.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return
    
    resultado = fatorial(n)
    print(f"{n}! = {resultado}")

if __name__ == "__main__":
    calcular_fatorial()