def num_positivos(list):
    list2 = []

    for i in range(len(list)):
        if (list[i] >= 0):
           list2.append(list[i])

    return list2

tam = int(input(" Informe o tamanho da lista: "))
lista = []

for i in range(tam):
    num = int(input(f" Informe o {i+1}º número da lista: ")
    lista.append(num)

print(f" Lista original: {lista}")

lista2 = num_positivos(lista)

print(f" Lista modificada: {lista2}")
