nome = input("Informe o seu nome: ")
idade =  int(input("Informe a sua idade: "))
sexo = input("Informe o seu sexo (M/F): ")

print(f"\nNome: {nome.title()}\n")
print(f"Idade: {idade} anos")
if(idade<18):
  print("Faixa etária: Menor de idade\n")  
elif (idade>=18 and idade<=64):
  print("Faixa etária: Maior de idade\n")
else:
  print("Faixa etária: Idoso(a)\n") 

if(sexo=='m' or sexo=='M'):
  print("Sexo: Masculino")
else:
  print("Sexo: Feminino")  

print("\n Fim do programa!")  