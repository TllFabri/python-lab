def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def tabela_fatoriais():
    print("Tabela de Fatoriais de 0 a 10:")
    for n in range(11):
        print(f"{n}! = {fatorial(n)}")

if __name__ == "__main__":
    tabela_fatoriais()