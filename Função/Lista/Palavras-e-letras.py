def inverter_letras(texto: str) -> str:
    return texto[::-1]

def inverter_palavras(frase: str) -> str:
    palavras = frase.split()
    return " ".join(palavras[::-1])

entrada = input("Digite uma palavra ou frase: ")

print("\n(a) Letras invertidas:")
print(inverter_letras(entrada))

print("\n(b) Palavras invertidas:")
print(inverter_palavras(entrada))
