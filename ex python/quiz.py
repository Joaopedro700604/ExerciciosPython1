def quiz():

    pontuacao = 0

    resposta = input("Capital do Brasil: ").lower()

    if resposta == "brasilia":
        pontuacao += 1

    resposta = input("Quanto é 5x5? ")

    if resposta == "25":
        pontuacao += 1

    print(f"Pontuação final: {pontuacao}")
    
quiz()