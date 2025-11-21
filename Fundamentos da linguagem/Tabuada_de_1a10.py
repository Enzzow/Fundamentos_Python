num = int(input("Informe um número para obter a tabuada de 1 a 10: "))
print(f"\nTabuada de {num}:\n")
for i in range (1,11):
  multp = num*i
  print(f"{num} x {i} = {multp}\n") 
  