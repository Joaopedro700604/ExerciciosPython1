import time
def cronometro():

    try:
        segundos = int(input("Digite os segundos: "))

    except ValueError:
        print("Digite apenas números!")
        return

    while segundos > 0:

        print(segundos)

        time.sleep(1)

        segundos -= 1

    print("Tempo encerrado!")

cronometro()
    
    