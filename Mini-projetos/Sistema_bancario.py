# =========================
#        FUNÇÕES DO MENU
# =========================

def menu():
    print("\n   #====Menu====#\n")
    print("   [1] Depositar") 
    print("   [2] Extrato")
    print("   [3] Saque")
    print("   [4] Criar Usuário")
    print("   [5] Criar Conta Corrente")
    print("   [6] Sair")


# =========================
#        USUÁRIOS
# =========================

def menu_usuario(lista):
    if len(lista) > 0:
        print("\n Deseja criar outro usuário?\n")
    else:
        print("\n Deseja criar usuário?\n")
    print(" [s] Sim")
    print(" [n] Não")


def criar_usuario(lista):
    print("\n ** Criando usuário...  \n")
    usuario = {}
    
    usuario["Nome"] = input(" Informe o nome de usuário: ").title()
    usuario["Data"] = input(" Informe a data de nascimento (dd/mm/aaaa): ")
    usuario["Endereço"] = input(" Informe o seu endereço: ")
    cpf = int(input(" Informe o CPF: "))
    
    repet = True
    while repet:
        repet = False
        for i in lista:
            if i["CPF"] == cpf:
                print("\n Já existe um usuário cadastrado com esse CPF!\n")
                repet = True
                cpf = int(input(" Informe outro CPF: "))
                break

    usuario["CPF"] = cpf
    return usuario


def add_usuarios(lista, usuario):
    lista.append(usuario)


# =========================
#     CONTAS CORRENTES
# =========================

def criar_conta_corrente(usuarios, contas):
    print("\n ** Criando conta corrente... \n")

    cpf = int(input(" Informe o CPF do usuário: "))

    usuario_encontrado = None
    for u in usuarios:
        if u["CPF"] == cpf:
            usuario_encontrado = u
            break

    if not usuario_encontrado:
        print("\n Usuário não encontrado! Cadastre o usuário antes.\n")
        return None

    conta = {
        "agencia": "0001",
        "numero_da_conta": len(contas) + 1,
        "usuario": usuario_encontrado
    }

    contas.append(conta)
    print("\n Conta criada com sucesso!\n")
    print(f" Agência: {conta['agencia']}")
    print(f" Número da conta: {conta['numero_da_conta']}")
    print(f" Usuário: {conta['usuario']['Nome']}")
    return conta


# =========================
#   FUNÇÕES BANCÁRIAS
# =========================

def deposito(saldo, valor):
    saldo += valor
    print(f"\n | Depósito de R$ {valor:.2f} realizado com sucesso! |")
    return saldo

def saque(saldo, valor_saque):
    saldo -= valor_saque
    print(f"\n | Saque de R$ {valor_saque:.2f} realizado com sucesso! |")
    return saldo

def extrato(saldo):
    print(f"\n | Saldo atual: R$ {saldo:.2f} |")


# =========================
#         PROGRAMA
# =========================

usuarios = []
contas = []
saldo = 0.00

menu()
opcao = int(input("\n Selecione uma das opções do menu acima: "))
continua = True

while continua:
    
    while opcao not in [1, 2, 3, 4, 5, 6]:
        print("\n  Opção inválida!\n")
        opcao = int(input("\n Digite uma opção válida do menu: "))
        
    if opcao == 6:
        continua = False
        print("\n Fim da sessão! :D")

    else:

        if opcao == 2:
            extrato(saldo)

        elif opcao == 1:
            print("\n | OBS: Limite de depósito é de R$ 50.000,00 |\n")    
            valor = float(input(" Informe o valor que deseja depositar: R$ "))
          
            while valor <= 0.0 or valor > 50000:
                print("\n | Valor inválido! |")
                valor = float(input(" Informe um valor válido para depósito: R$ "))
              
            saldo = deposito(saldo, valor)
          
        elif opcao == 3:
            if saldo == 0.0:
                print("\n | Você não possui saldo! |\n")
            else:
                valor_saque = float(input("\n Informe o valor que deseja retirar: R$ "))
             
                if valor_saque > saldo or valor_saque <= 0.0:
                    print("\n | Saque inválido! |\n")
                else:
                    saldo = saque(saldo, valor_saque)

        elif opcao == 4:
            novo = criar_usuario(usuarios)
            add_usuarios(usuarios, novo)

        elif opcao == 5:
            criar_conta_corrente(usuarios, contas)
                 
        menu()
        opcao = int(input("\n Digite uma das opções do menu acima: "))
