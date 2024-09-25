menu = """
Sistema Bancário
-
Opções:
1 - Sacar
2 - Depositar
3 - Emitir extrato
0 - Sair
-
Informe uma opção: """

saldo = 0
qtde_limite_saques = 3
valor_maximo_saque = 500.0
contador_saques = 1
extrato = "Saldo inicial:\t\t R$ " + str(f"{saldo:10.2f}\n")

opcao = "9"

while (opcao):
    opcao = int(input(menu))
    print("-")
    if (opcao == 1):
        valor = float(input(f"Saque\n-\nSaldo disponível: R$ {saldo:.2f}\n\nInforme o valor do saque: R$ "))

        if (contador_saques > qtde_limite_saques):
            print(f"-\nQuantidade de saques diários ({qtde_limite_saques}) foi excedida!\nTente novamente amanhã!\n")
            continue
        elif (valor > valor_maximo_saque):
            print(f"-\nO valor máximo por saque (R$ {valor_maximo_saque:.2f}) foi excedido.\nDigite um valor menor!\n")
            continue
        elif (valor > saldo):
            print(f"-\nO valor informado excede o saldo disponível (R$ {saldo:.2f}).\nDigite um valor menor ou igual ao saldo!\n")
            continue
        else:
            extrato += f"Saque:\t\t\t(R$ {valor:10.2f})\n"
            saldo -= valor
            contador_saques += 1
    elif (opcao == 2):
        valor = float(input(f"Depósito\n-\nSaldo disponível: R$ {saldo:.2f}\n\nInforme o valor do depósito: R$ "))
        if (valor > 0):
            extrato += str(f"Depósito:\t\t R$ {valor:10.2f}\n")
            saldo += valor 
        else:
            print("Informe um valor maior que 0(zero)!")               
    elif (opcao == 3):
        print("Extrato\n-")
        print(f"{extrato}Saldo final:\t\t R$ {saldo:10.2f}\n")
    elif (opcao == 0):
        print("Sistema encerrado!\n")
        break
    else:
        print("Você informou uma opção inválida!\nTente novamente!\n")

    



