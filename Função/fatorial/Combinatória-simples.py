from math import factorial

def ler_palavra_sem_repeticao():
    while True:
        palavra = input("Digite uma palavra sem letras repetidas: ").strip()
        if not palavra.isalpha():
            print("Use apenas letras (sem espaços, números ou símbolos).")
            continue
        base = palavra.lower()
        if len(set(base)) != len(base):
            print("A palavra possui letras repetidas. Tente outra (ex.: 'amor').")
            continue
        return palavra

def quantidade_anagramas_sem_repeticao(palavra: str) -> int:
    return factorial(len(palavra))

palavra = ler_palavra_sem_repeticao()
qtd = quantidade_anagramas_sem_repeticao(palavra)
print(f"A palavra '{palavra}' tem {qtd} anagramas possíveis.")
