def eh_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    return texto == texto[::-1]

def contador_palindromos():
    try:
        n = int(input("Digite o número de palavras: "))
        if n <= 0:
            print("Por favor, insira um número positivo.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        return
    
    contador = 0

    for i in range(n):
        palavra = input(f"Digite a palavra {i+1}: ")
        if eh_palindromo(palavra):
            contador += 1

    porcentagem = (contador / n) * 100 if n > 0 else 0

    print(f"\nTotal de palavras: {n}")
    print(f"Palíndromos encontrados: {contador}")
    print(f"Porcentagem de palíndromos: {porcentagem:.2f}%")

if __name__ == "__main__":
    contador_palindromos()
    


