def conversor_temperatura():

    print("\n1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")

    opcao = input("Escolha: ")

    try:

        if opcao == "1":

            c = float(input("Celsius: "))

            f = (c * 9/5) + 32

            print(f"Fahrenheit: {f:.2f}")

        elif opcao == "2":

            f = float(input("Fahrenheit: "))

            c = (f - 32) * 5/9

            print(f"Celsius: {c:.2f}")

        else:
            print("Opção inválida")

    except ValueError:
        print("Digite apenas números!")
conversor_temperatura()