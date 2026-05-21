def numero_primo():

    numero = int(input("Digite um número: "))

    contador = 0

    for i in range(1, numero + 1):

        if numero % i == 0:
            contador += 1

    if contador == 2:
        print("Número primo")

    else:
        print("Não é primo")


numero_primo()