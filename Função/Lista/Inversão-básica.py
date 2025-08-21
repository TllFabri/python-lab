def inverter_lista(lista):
    return lista[::-1]

entrada = input("Digite números inteiros separados por espaço: ")

numeros = [int(x) for x in entrada.split()]

invertida = inverter_lista(numeros)

print("Lista original:", numeros)
print("Lista invertida:", invertida)
