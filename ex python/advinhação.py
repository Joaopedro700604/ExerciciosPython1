import random
def adivinhe_numero():

    numero = random.randint(1, 100)

    while True:

        try:
            tentativa = int(input("Digite um número entre 1 e 100: "))

        except ValueError:
            print("Digite apenas números inteiros!")
            continue

        if tentativa == numero:
            print("Você acertou!")
            break

        elif tentativa < numero:
            print("Maior...")

        else:
            print("Menor...")

adivinhe_numero()