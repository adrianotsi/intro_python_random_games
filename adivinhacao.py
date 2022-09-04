import random
def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("***********************************")

    secret_number = random.randrange(1, 101)
    attempts = 3
    # round = 1

    # while(round <= attempts):
    for round in range(1, attempts+1):
        print("E lá vamos nóóós tentativa {} de {}".format(round, attempts))

        shot = int(input("Digite o seu número meu consagrado entre 1 e 100:"))

        print("Você digitou ", shot)

        if(shot < 1 or shot > 100):
            print("Prestenção bixo, entre 1 e 100!")
            continue

        is_correct = secret_number == shot
        is_more = shot > secret_number
        is_less = shot < secret_number

        if (is_correct):
            print("BIN BIN BIN ACERTOU!")
            break
        else:
            if(is_more):
                print("ERROOOW! Mutcho alto my camaradinha")
            elif(is_less):
                print("ERRRROW! Mutcho poco my camaradinha")

            # round = round + 1

    print("Todo mundo morreu! Acabo.")

if(__name__ == "__main__"):
    jogar()
