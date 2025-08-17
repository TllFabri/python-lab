frase = input("Digite uma frase: ")
frase_limpa = frase.replace(" ", "").lower()
frase_invertida = frase_limpa[::-1]

if frase_limpa == frase_invertida:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")