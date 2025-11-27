def retornar_maior(lista):
    maior = lista[0]

    for i in range(len(lista-1)):
        if maior<lista[i+1]:
            maior = lista[i+1]
    
    return maior

lista = []
tam = int(input(" \nInforme o tamanho da lista: "))

for i in range(tam):
    num = int(input(f" Digite o {i+1}º número da lista: "))
    lista.append(num)

print("\n")
print(f" O maior número da lista é {retornar_maior(lista)}\n")

