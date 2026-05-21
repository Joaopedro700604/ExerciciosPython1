compras = []

def lista_compras():

    while True:

        print("\n1 - Adicionar")
        print("2 - Mostrar")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            item = input("Digite o item: ")

            compras.append(item)

        elif opcao == "2":

            print("\nLista de Compras:")

            for item in compras:
                print("-", item)

        elif opcao == "3":
            break

        else:
            print("Opção inválida")


lista_compras()