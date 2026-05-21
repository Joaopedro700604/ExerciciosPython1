import random

def pedra_papel_tesoura():

    opcoes = ["pedra", "papel", "tesoura"]

    while True:

        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if jogador not in opcoes:
            print("Opção inválida!")
            continue

        computador = random.choice(opcoes)

        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate!")

        elif (
            (jogador == "pedra" and computador == "tesoura") or
            (jogador == "papel" and computador == "pedra") or
            (jogador == "tesoura" and computador == "papel")
        ):
            print("Você venceu!")

        else:
            print("Você perdeu!")

        continuar = input("Continuar? (sim/nao): ")

        if continuar.lower() != "sim":
            break

pedra_papel_tesoura()