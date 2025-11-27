def retornar_maior(lista):
    maior = 0

    for i in range(len(lista)):
        if maior<lista[i]:
            maior = lista[i]
    
    return maior

lista = []
tam = int(input(" \nInforme o tamanho da lista: "))

for i in range(tam):
    num = int(input(f" Digite o {i+1}º número da lista: "))
    lista.append(num)

print("\n")
print(f" O maior número da lista é {retornar_maior(lista)}\n")

