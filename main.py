import credits
import adivinhacao
import forca

def escolhe_jogo():
    print("*********************************")
    print("******AAALO! How you doing?******")
    print("*********************************")

    print("[1] Jogar adivinhação [2] Jogar advinhação (Com resposta) [3] Jogar Forca [4] Créditos")

    opt = int(input("Selecione uma opção: "))

    if(opt == 1):
        print("SHOW! Vamos jogar adivinhaçãoo")
        adivinhacao.jogar()
    elif(opt == 2):
        print("Ok então vamos jogar adivinhaçãooo, mas exibindo a resposta")
        adivinhacao.jogar(True)
    elif (opt == 3):
        print("Ok então vamos jogar Forca!!")
        forca.jogar()
    elif (opt == 4):
        print("... segue os créditos")
        credits.show()

if(__name__ == "__main__"):
    escolhe_jogo()
