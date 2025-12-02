#def valor_menor(*numeros):
    #print(f"\n O menor número é {min(numeros)} \n")

#valor_menor(2,1,5,4,-1)

def valor_menor(*numeros):
    menor = numeros[0]

    for numero in numeros[1:]:
        if menor>numero:
            menor = numero
    
    print(f"\n O menor número é {menor} \n")

valor_menor(2,1,0,-1,100,-2)