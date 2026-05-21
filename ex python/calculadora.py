def calculadora():

    while True:

        print("\n1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        opcao = input("Escolha: ")

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida")
            continue

        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))

        if opcao == "1":
            resultado = n1 + n2

        elif opcao == "2":
            resultado = n1 - n2

        elif opcao == "3":
            resultado = n1 * n2

        elif opcao == "4":

            if n2 == 0:
                print("Não existe divisão por zero.")
                continue

            resultado = n1 / n2

        print(f"Resultado: {resultado:.2f}")

        sair = input("Deseja sair? (s/n): ")

        if sair.lower() == "s":
            break


calculadora()