import random

def sorteador():

    alunos = []

    quantidade = int(input("Quantidade de alunos: "))

    for i in range(quantidade):

        nome = input("Nome do aluno: ")

        alunos.append(nome)

    sorteado = random.choice(alunos)

    print("Aluno sorteado:", sorteado)


sorteador()