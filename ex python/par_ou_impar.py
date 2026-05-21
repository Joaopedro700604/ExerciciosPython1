import random

def par_ou_impar():

    while True:

        jogador = int(input("Digite um número: "))

        escolha = input("Par ou ímpar? ").lower()

        computador = random.randint(1, 10)

        soma = jogador + computador

        print(f"Computador escolheu {computador}")
        print(f"Soma = {soma}")

        if soma % 2 == 0 and escolha == "par":
            print("Você venceu!")

        elif soma % 2 != 0 and escolha == "ímpar":
            print("Você venceu!")

        else:
            print("Você perdeu!")

        sair = input("Continuar? (s/n): ").lower()

        if sair != "s":
            break


par_ou_impar()