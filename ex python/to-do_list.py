tarefas = []


def adicionar_tarefa():

    tarefa = input("Digite a tarefa: ")

    if tarefa == "":
        print("Digite uma tarefa válida.")
        return

    tarefas.append(tarefa)

    print("Tarefa adicionada!")


def listar_tarefas():

    if len(tarefas) == 0:

        print("Nenhuma tarefa cadastrada.")

    else:

        print("\n===== TAREFAS =====")

        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i} - {tarefa}")

        print(f"\nTotal de tarefas: {len(tarefas)}")


def remover_tarefa():

    listar_tarefas()

    if len(tarefas) == 0:
        return

    try:
        indice = int(input("Digite o número da tarefa: "))

        indice -= 1

    except ValueError:

        print("Digite apenas números!")

        return

    if 0 <= indice < len(tarefas):

        tarefa_removida = tarefas.pop(indice)

        print(f"Tarefa '{tarefa_removida}' removida!")

    else:
        print("Índice inválido")


def todo_list():

    while True:

        print("\n===== TO-DO LIST =====")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Remover")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            remover_tarefa()

        elif opcao == "0":

            print("Programa encerrado!")

            break

        else:
            print("Opção inválida")


todo_list()