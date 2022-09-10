import random
def jogar():
    print("**********************************")
    print("*******Jogo de Forca 💀!*******")
    print("**********************************")

    secret_word = load_secret_word()
    incomplete_word = ["_" for caracter in secret_word]

    game_over = False
    victory = False
    errors = 0

    while(not game_over and not victory):
        shot = input("Qual letra? ").strip().upper()

        index = 0
        if(shot in secret_word):
            for caractere in secret_word:
                if(shot == caractere):
                    incomplete_word[index] = caractere
                index += 1
        else:
            errors += 1
            draw_forca(errors)

        game_over = errors == 7
        victory = "_" not in incomplete_word
        print(incomplete_word)

    if(victory):
        print("Aeeoh você acertou!")
    else:
        print("Valeu a tentativa, mas tu perdue :c a palavra era {}".format(secret_word))
    print("Game over")

def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    secret_word = words[random.randrange(0, len(words))].upper()
    return secret_word

def draw_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
