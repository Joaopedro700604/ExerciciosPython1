def media_notas():

    notas = []

    for i in range(3):

        nota = float(input(f"Digite a nota {i+1}: "))

        notas.append(nota)

    media = sum(notas) / len(notas)

    print(f"Média: {media:.2f}")


media_notas()