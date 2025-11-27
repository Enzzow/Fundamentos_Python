materias = {
    "Português": 7.5,
    "Matemática": 7.9,
    "Ciências": 8.2,
    "História": 8.0,
    "Geografia": 7.2,
    "Inglês": 6.0
}

nome = input("\n Informe o nome do aluno: ")

soma = 0
for chave,valor in materias.items():
    soma+=valor

media = soma/len(materias)
    
