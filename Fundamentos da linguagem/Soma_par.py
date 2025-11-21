tam = int(input(" Informe o tamanho da lista: ")) 

while (tam<=0 and tam>10): 
    tam = int(input(" Informe o tamanho da lista: "))

lista = []

for i in range(0,tam):
    num = int(input(f" Digite o {i+1}º número da lista: "))
    lista.append(num)

soma = 0

for ii in range(0,tam):
    if (lista[ii]%2==0):
      soma = soma+lista[ii]

print(f" A soma entre os números pares corresponde a {soma}")
