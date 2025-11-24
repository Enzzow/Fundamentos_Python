TAM = 4

lista = []
soma = 0


for i in range(TAM):
    num = int(input(f" Digite o {i+1}º número da lista: "))
    soma += num
    lista.append(num)

media = soma/TAM

print(f"\n Lista: {lista}")
print(f" Média dos números da lista: {media:.2f} \n")

maiores = []
qntd = 0
for i in range(TAM):
    if lista[i]>media:
      maiores.append(lista[i])
      qntd+=1

if qntd > 0:
   print(f" Nº de números maiores que a média: {qntd}")
   print(f" Número(s) maior(es) que a média: {maiores}\n")
else:
   print(" Nenhum número da lista é maior que a média.\n")



