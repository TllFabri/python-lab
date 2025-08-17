def eh_palindromo(texto):
    frase_limpa = texto.replace(" ", "").lower()
    frase_invertida = frase_limpa[::-1]
    return frase_limpa == frase_invertida

frases = [
    "Ame a ema",
    "Socorram-me, subi no ônibus em Marrocos",
    "Python",
    "Ana",
    "Ovo"
]

print("Relatório de Palíndromos:")
for f in frases:
    if eh_palindromo(f):
        print(f"'{f}' → É palíndromo")
    else:
        print(f"'{f}' → Não é palíndromo")
