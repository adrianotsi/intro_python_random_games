import random
import main
def jogar(showSecret=False):
    assert isinstance(showSecret, bool)

    print("**********************************")
    print("*******Jogo de Adivinhação!*******")
    print("**********************************")
    print("\n")
    print("??????????????????????????????????")
    print("O script vai gerar um número aleatório entre 1 e 100, consegue adivinha? am? heim? heim?")
    print("??????????????????????????????????")
    print("\n")
    print("Qual nível de dificuldade você quer jogar?")
    print("[1] Fácil [2] Médio [3] Difícil")

    level = int(input("Informe o nível: "))

    # Define quantidade de tentativas com base no nível
    if(level == 1):
        attempts = 15
        print("BONITO! Você vai ter {} tentativas para adivinhar o número gerado".format((attempts)))
    elif(level == 2):
        attempts = 10
        print("SHOW! Você vai ter {} tentativas para adivinhar o número gerado".format((attempts)))
    elif (level == 3):
        attempts = 5
        print("OLOCO! Você vai ter {} tentativas para adivinhar o número gerado".format((attempts)))

    # Gerando número
    secret_number = random.randrange(1, 101)

    # Exibe resposta
    if(showSecret == True):
        print("Não conta pra ninguém, o número gerado foi {}".format(secret_number))

    for round in range(1, attempts + 1):
        print("E lá vamos nóóós tentativa {} de {}".format(round, attempts))

        shot = int(input("Digite o seu número meu consagrado entre 1 e 100:"))

        print("Você digitou ", shot)

        if (shot < 1 or shot > 100):
            print("Prestenção bixo, entre 1 e 100!")
            continue

        is_correct = secret_number == shot
        is_more = shot > secret_number
        is_less = shot < secret_number

        if (is_correct):
            print("BIN BIN BIN ACERTOU!")
            break
        else:
            if(round == attempts):
                print("Ninguém acertouuu, acabaram as tentativas :c")
                continue
            if (is_more):
                print("ERROOOU! Mutcho alto, tenta um número menor aí")
            elif (is_less):
                print("ERRRROU! Mutcho poco, tenta um número maior aí")

    print("O número gerado era {}. Todo mundo morreu! Acabo.".format(secret_number))

    print("...voltando para o menu principal")

    main.escolhe_jogo()

if (__name__ == "__main__"):
    jogar()
