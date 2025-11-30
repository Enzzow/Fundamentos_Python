def menu():
    print(" \n   #====Menu====#\n")
    print("   [1] Depositar ") 
    print("   [2] Extrato   ") 
    print("   [3] Saque     ") 
    print("   [4] Sair      ")

def deposito(saldo, valor):
    saldo += valor
    print(f" \n | Deposito de R$ {valor:.2f} realizado com sucesso! |")
    return saldo

def saque(saldo, valor_saque):
    saldo -= valor_saque
    print(f" \n | Saque de R$ {valor_saque:.2f} realizado com sucesso! |")
    return saldo

def extrato(saldo):
    print(f" \n | Saldo atual de R$ {saldo:.2f} | ")

menu()
opcao = int(input(" \n Selecione uma das opções do menu acima: "))
continua = True

saldo = 0.00

while continua:
    
    while opcao not in [1, 2, 3, 4]:
        print(" \n  Opção inválida!\n")
        opcao = int(input(" \n Digite uma das opções do menu acima: "))
        
    if opcao == 4:
        continua = False
        print(" \n Fim da sessão! :D")

    else:

        if opcao == 2:
            extrato(saldo)
          
        elif opcao == 1:
            print(" \n | OBS: Limite de deposito é de R$ 50.000,00 |\n ")    
            valor = float(input(" Informe o valor que deseja depositar: R$ "))
          
            while valor <= 0.0 or valor > 50000:
                print("\n | Valor inválido! |")
                valor = float(input(" \n Informe o valor que deseja depositar: R$ "))
              
            saldo = deposito(saldo, valor)
          
        elif opcao == 3:
            if saldo == 0.0:
                print(" \n | Você não possui saldo! |\n")
            else:
                valor_saque = float(input(" \n Informe o valor que deseja retirar: R$ "))
             
                if valor_saque > saldo or valor_saque <= 0.0:
                    print(" \n | Saque inválido! |\n")
                else:
                    saldo = saque(saldo, valor_saque)
                 
        menu()
        opcao = int(input(" \n Digite uma das opções do menu acima: "))
