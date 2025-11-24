continua = True
soma = 0
cont = 1

while continua:
  
  num = int(input(f" Informe o {cont}º número: ")
  soma += num

  print(" Deseja continuar ?")
  decisao = input(" Digite 'S' para continuar ou 'N' para encerrar o programa: ").lower()

  if decisao != 's' and decisao != 'n':
    
    print( " Inválido!")
    
    while decisao != 's' and decisao != 'n':
      decisao = input(" Digite 'S' para continuar ou 'N' para encerrar o programa: ").lower()
      
  elif decisao == 's':
    cont+=1
  else:
    continua = False

print(f" Resultado da soma = {soma}")
print(" Fim do programa!")
