armario = {
    "Arroz":1,
    "Feijão":3,
    "Macarrão":2,
    "Açúcar":1
}

alimento = input("\n Informe o alimento que deseja: ").title()

if alimento in armario:
    print(f" Possuí {armario[alimento]} em estoque\n")
else:
    print(f" Fora de estoque!\n")
