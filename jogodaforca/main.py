import os
import database
import random
import jogo


def _choose_random_word():
    num_words = len(database.words)
    index_random_word = random.randint(0, num_words-1)
    return database.words[index_random_word]


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    start = input(
        '\nVocê deseja iniciar um jogo de forca? [S/N] ').upper().strip()


    if start == 'GO':
        word = _choose_random_word()
        game.play(word.upper())

    elif start == 'Exit':
        print('Fechando o jogo...')
        exit()

    else:
        print('Essa opcao nao existe!')
