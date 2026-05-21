def contador_palavras():

    texto = input("Digite um texto: ")

    palavras = texto.split()

    print(f"Quantidade de palavras: {len(palavras)}")

    print(f"Quantidade de letras: {len(texto)}")
    
contador_palavras()