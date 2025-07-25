import random

def guessing_game():
    # Gerando número aleatório entre 1 e 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100")
    
    while True:
        # Recebendo palpite do usuário
        try:
            guess = int(input("Digite seu palpite: "))
            attempts += 1
            
            # Verificando o palpite
            if guess == secret_number:
                print(f"Parabéns! Você acertou em {attempts} tentativas!")
                break
            elif guess < secret_number:
                print("Tente um número MAIOR!")
            else:
                print("Tente um número MENOR!")
                
        except ValueError:
            print("Por favor, digite apenas números inteiros!")
            
# Iniciando o jogo
guessing_game()