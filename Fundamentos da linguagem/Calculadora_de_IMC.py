print("\n &| Calculadora de Índice de massa corporal(IMC) |&  \n")
nome = input(" Informe o seu nome: ")

idade = int(input(" Informe a sua idade: "))
while(idade<=0):
  print(" Inválido!\n")
  idade = int(input(" Informe a sua idade: "))

altura = float(input(" Informe a sua altura em m(metros): "))
while(altura<=0):
 print(" Inválido!\n")
 altura = float(input(" Informe a sua altura: "))

peso = float(input(" Informe o seu peso em kg(quilograma): "))
while(peso<=0):
  print(" Inválido!\n")
  peso = float(input(" Informe o seu peso: "))

imc = peso/pow(altura,2)

print(" Dados do paciente:\n")
print(f" Nome: {nome}\n")
print(f" Idade: {idade}\n")
print(f" Altura: {altura:.2f} m\n")
print(f" Peso: {peso:.2f} kg\n")


print(" Situação: ")

if (imc<18.5):
  print("Abaixo do peso\n")
elif (imc>=18.5 and imc<=24.9):
  print("Peso normal\n")
elif (imc>=25.0 and imc<=29.9):
  print("Sobrepeso\n")
elif (imc>=30.0 and imc<=34.9):
  print("Obesidade grau I\n")
elif (imc>=35.0 and imc<=39.9):
  print("Obesidade grau II\n")
else:
  print("Obesidade grau III\n")  
