import credits
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******AAALO!*******")
    print("*********************************")

    print("[1] Jogar adivinhação [2] Créditos]")

    opt = int(input("Selecione uma opção: "))

    if(opt == 1):
        print("Jogar adivinhaçãooo")
        adivinhacao.jogar()
    elif(opt == 2):
        print("Créditos")
        credits.show()

if(__name__ == "__main__"):
    escolhe_jogo()
