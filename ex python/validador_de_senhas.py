def validar_senha():

    senha = input("Digite uma senha: ")

    if len(senha) >= 8:
        print("Senha forte")

    else:
        print("Senha fraca")


validar_senha()