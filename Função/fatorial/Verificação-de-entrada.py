def ler_inteiro_positivo():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            if num < 0:
                print("Número negativo não é permitido. Digite novamente.")
            else:
                return num
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

numero = ler_inteiro_positivo()
print(f"Você digitou {numero}, entrada aceita!")
