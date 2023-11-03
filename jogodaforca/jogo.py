import os


def _verify_endgame(word, check_word_in_used_letters, num_lifes):
    word_only_alpha = [c.lower() for c in word if c.isalpha()]

    if check_word_in_used_letters == len(word_only_alpha):
        print('> Parabéns você venceu')
        return True
    if num_lifes == 0:
        print('> Acabaram suas chances')
        return True
    else:
        return False
      
def _print_word_status(word, num_lifes, used_letters):

    if num_lifes == 6:
        print('            ______         ')
        print('           /      |        ')
        print('           |               ')
        print('           |               ')
        print('           |               ')
        print('           |               ')
        print('                           ')

    elif num_lifes == 5:
        print('            ______         ')
        print('           /      |        ')
        print('           |      O        ')
        print('           |               ')
        print('           |               ')
        print('           |               ')
        print('                           ')

    elif num_lifes == 4:
        print('            ______         ')
        print('           /      |        ')
        print('           |      O        ')
        print('           |      I        ')
        print('           |      I        ')
        print('           |               ')
        print('                           ')

    elif num_lifes == 3:
        print('            ______         ')
        print('           /      |        ')
        print('           |      O        ')
        print('           |    / I        ')
        print('           |      I        ')
        print('           |               ')
        print('                           ')

    elif num_lifes == 2:
        print('            ______         ')
        print('           /      |        ')
        print('           |      O        ')
        print('           |    / I \      ')
        print('           |      I        ')
        print('           |               ')
        print('                           ')

    elif num_lifes == 1:
        print('            ______         ')
        print('           /      |        ')
        print('           |      O        ')
        print('           |    / I \      ')
        print('           |      I        ')
        print('           |    /          ')
        print('                           ')

    elif num_lifes == 0:
        print('            ______         ')
        print('           /      |        ')
        print('           |      O        ')
        print('           |    / I \      ')
        print('           |      I        ')
        print('           |    /   \      ')
        print('                           ')

    print('# Palavra secreta: ', end='')
    for i in word:
        if i in used_letters:
            print(f'{i}', end='')
        elif not i.isalpha():
            print(f'{i}', end='')
        else:
            print(' _', end='')
    print('')

    print(f'# Você tem {num_lifes} chances')
    print('# Letras ja digitadas: ', end='')
    for i in used_letters:
        print(i, end=', ')
    print('\n')


def _get_letter(used_letters):
    while True:
        last_letter = input('Digite uma letra: ').upper()[0]
        if last_letter in used_letters:
            print('> A letra já foi selecionada\n')
        elif not last_letter.isalpha():
            print('> Caracter invalido\n')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return last_letter


def play(word):
    # Function that has the logic of the game
    # Checks if the letter typed matches the word
    # And gives feedback to the player according to the result

    num_lifes = 6
    used_letters = []
    _print_word_status(word, num_lifes, used_letters)

    while True:
        flag_correct_letter_attempt = False
        check_word_in_used_letters = 0

        last_letter = _get_letter(used_letters)
        used_letters.append(last_letter)

        for i in word:
            if i == last_letter:
                flag_correct_letter_attempt = True
            if i in used_letters:
                check_word_in_used_letters += 1

        if not flag_correct_letter_attempt:
            num_lifes -= 1
            print('> Você errou a letra')

        if _verify_endgame(word, check_word_in_used_letters, num_lifes): break

        _print_word_status(word, num_lifes, used_letters)

    _print_word_status(word, num_lifes, used_letters)
