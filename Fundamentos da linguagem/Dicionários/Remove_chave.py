frutas = {
    "Maça": 2.50,
    "Uva": 2.50, 
    "Peira": 3.50,
    "Melancia": 10.00,
    "Arroz": 5.00
}

print(f"\nEstoque de frutas original:\n")

print(frutas)

valor = frutas.pop("Arroz")# Obtém o valor do Arroz

#Adiciona a nova fruta e atribui o valor que pertencia ao arroz
frutas["Acerola"] = valor 

print("\n Estoque de frutas modificado:\n")
print(f"{frutas}\n")
