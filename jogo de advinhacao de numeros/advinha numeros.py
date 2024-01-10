

import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Defina o número máximo de tentativas

    print("Bem-vindo ao Jogo de Adivinhação!")
    print(f"Tente adivinhar um número entre 1 e 100. Você tem {max_attempts} tentativas.")

    while attempts < max_attempts:
        try:
            guess = int(input("Digite um número: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        attempts += 1

        if guess < number:
            print("Muito baixo. Tente novamente.")
        elif guess > number:
            print("Muito alto. Tente novamente.")
        else:
            print(f"Parabéns! Você acertou em {attempts} tentativas.")
            break
    else:
        print(f"Você atingiu o número máximo de tentativas. O número era {number}.")

guess_the_number()
