tam = int(input("Informe o tamanho da lista: "))
lista = []

for i in range(tam):
    num = int(input(f"Digite o {i+1}º número da lista: "))
    lista.append(num)

print(f"Lista original: {lista}")

lista2 = []

for i in range(tam):
    repet = False        
    ii = i + 1

    while not repet and ii < tam:
        if lista[i] == lista[ii]:
            repet = True
        ii += 1          

    if not repet:
        lista2.append(lista[i])

print(f"Lista modificada: {lista2}")
