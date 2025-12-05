def apresentacao(func):
    def wrapper():
        print(" \n Teste: ",end="")
        func()

    return wrapper

@apresentacao #Açucar sintético(syntactic sugar) indicando que estou usando decorador
def teste():
    print("Funcionou!\n")

teste()