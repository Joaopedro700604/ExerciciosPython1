import random
import string
def gerador_senha():

    try:
        tamanho = int(input("Tamanho da senha: "))

    except ValueError:
        print("Digite apenas números!")
        return

    caracteres = string.ascii_letters + string.digits

    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    print("Senha gerada:", senha)
    
gerador_senha()
