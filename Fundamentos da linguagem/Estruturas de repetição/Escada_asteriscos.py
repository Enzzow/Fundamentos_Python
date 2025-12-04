def info():
    print("\n #=== Escada de asteriscos ===# \n")
    print("         # ATENÇÃO! #           ")
    print("     O limite de degraus é 10! \n")
    
def escada(num):
    
    print(" \n **Escada** \n")
    
    for i in range(num):
       for ii in range(i+1):
         print(" *",end="")
       print()

def menu_opcoes():
    print(" \n O que desejas fazer ? ( ͡° ͜ʖ ͡° )")
    print(" [1] Continuar")
    print(" [2] Sair\n")

    
num = 0
continua = True
while continua:
    
   info()
   while num<=0 or num>10:
     num = int(input(" Informe quantos degraus a escada de asteriscos deve ter: "))

   escada(num)
   
   menu_opcoes()
   opcao = int(input(" Escolha uma das opções do menu acima: "))
   
   while opcao not in [1,2]:
       print(" \n Opção inválida! \n")
       menu_opcoes()
       opcao = int(input(" Escolha uma das opções do menu acima: "))
   if opcao==2:
        print(" \n Fim do programa! \n")
        continua = False
   else:
        num = 0
   
   
   