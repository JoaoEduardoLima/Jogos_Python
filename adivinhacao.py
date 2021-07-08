import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    print()

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    nivel_str = ""
    if(nivel == 1):
        total_de_tentativas = 20
        nivel_str = "Fácil"
    elif(nivel == 2):
        total_de_tentativas = 10
        nivel_str = "Médio"
    else:
        total_de_tentativas = 5
        nivel_str = "Difícil"

    for rodada in range(1, total_de_tentativas + 1):
        print()
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos no nível {}.".format(pontos, nivel_str))
            print()
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                print()
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                print()
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("***********")
    print("Fim do jogo")
    print("***********")

if(__name__ == "__main__"):
    jogar()