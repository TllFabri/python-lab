def inverter_lista(lista):
    return lista[::-1]

frase = input("Digite uma frase: ")

palavras = frase.split()

invertidas = inverter_lista(palavras)

resultado = " ".join(invertidas)

print("Frase original:", frase)
print("Palavras invertidas:", resultado)
