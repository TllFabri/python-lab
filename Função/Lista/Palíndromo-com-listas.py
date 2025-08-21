def inverter_lista(lista):
    return lista[::-1]

def eh_palindromo(texto):
    lista = [c.lower() for c in texto if c.isalnum()]
    return lista == inverter_lista(lista)

entrada = input("Digite uma palavra ou frase: ")

if eh_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo!")
else:
    print(f"'{entrada}' não é um palíndromo.")
