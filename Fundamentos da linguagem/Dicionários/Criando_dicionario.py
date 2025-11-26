estoque = {}
tam = int(input(" Informe o número de produtos que irá registrar no estoque: "))

for i in range(tam):
    produto = input(f" Informe o nome do {i+1}º produto: ")
    estoque[i] = produto

    valor = int(input(f" Informe o valor do produto: "))
    estoque["produto"] = valor
    print("\n")


print(estoque)
