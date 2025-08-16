def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra: ")
print(eh_palindromo(palavra))